import java.util.*;
class File {
    String name[] =new String[30];  ;
    int nob[] =new int[30];
    int blocks[][]=new int[30][30];
    int n,i,j;
    Scanner sc=new Scanner(System.in);
     public void getname()
    {    System.out.println("\n Enter no of files");
          n=sc.nextInt();
        for( i=0;i<n;i++)
        {
        System.out.println("\n Enter file name");
        name[i]=sc.next();
        System.out.println("\n Enter no of blocks in file");
        nob[i]=sc.nextInt();
        System.out.println(" Enter blocks of file");
        for( j=0;j<nob[i];j++)
        blocks[i][j]=sc.nextInt();
    }

    }
    public void setname()
        {
          System.out.println("\n Enter file name to be searched");
          String fname=sc.next();
          for(i=0;i<n;i++)
          {
              String k=name[i];
              if(k.compareTo(fname)==0)
                  break;
          }
          if(i==n)
          {
             System.out.println("File not found");
              }
          else
          {
              System.out.println("\n File Name\t\tNo of Blocks\t\tBlocks Occupied");
               System.out.println("\t"+name[i]+"\t\t"+nob[i]);
               for(j=0;j<nob[i];j++)
                   System.out.println("\t\t\t\t\t\t\t"+blocks[i][j]);
}
}
}
public class NewClass1
{
    public static void main(String args[])
    {  
 File f=new File();
        f.getname();
        f.setname();
}
}
