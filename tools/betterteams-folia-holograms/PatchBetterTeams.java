import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.util.zip.*;
import org.objectweb.asm.*;
import org.objectweb.asm.tree.*;
public class PatchBetterTeams {
  public static void main(String[] args) throws Exception {
    Path src=Path.of(args[0]),out=Path.of(args[1]);
    int modified=0;
    try(ZipFile zip=new ZipFile(src.toFile()); ZipOutputStream result=new ZipOutputStream(Files.newOutputStream(out))) {
      Enumeration<? extends ZipEntry> entries=zip.entries();
      while(entries.hasMoreElements()) {
        ZipEntry entry=entries.nextElement();
        byte[] data=zip.getInputStream(entry).readAllBytes();
        if(entry.getName().equals("com/booksaw/betterTeams/Main.class")) {
          ClassNode node=new ClassNode(); new ClassReader(data).accept(node,0);
          for(MethodNode m:node.methods) {
            if(m.name.equals("setupHolograms") && m.desc.equals("()Z")) {
              m.instructions.clear();m.tryCatchBlocks.clear(); if(m.localVariables!=null)m.localVariables.clear();
              m.instructions.add(new InsnNode(Opcodes.ICONST_0));m.instructions.add(new InsnNode(Opcodes.IRETURN));
              m.maxStack=1; m.maxLocals=1;modified++;
            }
          }
          ClassWriter writer=new ClassWriter(0);node.accept(writer); data=writer.toByteArray();
        }
        ZipEntry item=new ZipEntry(entry.getName());result.putNextEntry(item);result.write(data);result.closeEntry();
      }
    }
    if(modified!=1)throw new IllegalStateException("Expected exactly one BetterTeams setupHolograms method; found "+modified);
    System.out.println("Patched one method to disable unsafe BetterTeams->DecentHolograms integration (not DecentHolograms itself)");
  }
}
