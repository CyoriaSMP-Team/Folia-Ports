#!/usr/bin/env bash
set -euo pipefail

# Verify upstream workflow changes are excluded, while code and Folia patches survive.
root="$(mktemp -d)"
trap 'rm -rf "$root"' EXIT
cd "$root"
git init -q
git config user.name 'CI Fixture'
git config user.email 'ci@example.invalid'
mkdir -p .github/workflows
printf 'folia-gate\n' > .github/workflows/ci.yml
printf 'original\n' > plugin.txt
git add .
git commit -qm base
git branch target
git branch upstream

git switch -q upstream
printf 'upstream-gate\n' > .github/workflows/ci.yml
printf 'upstream-new\n' > .github/workflows/new.yml
printf 'updated\n' > plugin.txt
git add .
git commit -qm upstream

git switch -q target
printf 'region-safe\n' > folia.patch
git add .
git commit -qm folia

for branch in build publish; do
  git switch -q target
  git switch -qc "$branch"
  git merge --no-ff --no-edit upstream >/dev/null
  git restore --source=target --staged --worktree -- .github/workflows
  if ! git diff --cached --quiet; then
    git commit --amend --no-edit >/dev/null
  fi
  test "$(cat .github/workflows/ci.yml)" = 'folia-gate'
  test ! -e .github/workflows/new.yml
  test "$(cat plugin.txt)" = 'updated'
  test "$(cat folia.patch)" = 'region-safe'
  test -z "$(git diff --name-only target HEAD -- .github/workflows)"
  printf '%s\n' "$(git rev-parse 'HEAD^{tree}')" > "$root/$branch.tree"
done
cmp "$root/build.tree" "$root/publish.tree"
echo 'PASS: workflows and Folia patch preserved; build/publish trees identical'
