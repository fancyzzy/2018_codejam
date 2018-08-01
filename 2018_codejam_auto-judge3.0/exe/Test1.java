import java.util.Scanner;
public class Test1 {
	private static char c;
	public static void main(String[] args) {
		@SuppressWarnings("resource")
		Scanner sc=new Scanner(System.in);
		System.out.println("请输入第一个字符串：");
		String s1=sc.nextLine();
		char a1[]=s1.toCharArray();
		int b1[] =new int[a1.length];
		for (int i = 0; i < a1.length; i++) 
		{
			b1[i]=a1[i];
		}
		int sum1=0;
		for (int i = 0; i <b1.length; i++) {
			sum1+=b1[i];
		}
		System.out.println("请输入第二个字符串：");
		String s2=sc.nextLine();
		char a2[]=s2.toCharArray();
		int b2[] =new int[a2.length];
		for (int i = 0; i < a2.length; i++) 
		{
			b2[i]=a2[i];
		}
		int sum2=0;
		for (int i = 0; i <b2.length; i++) {
			sum2+=b2[i];
		}
		c= (char)(sum2-sum1);
		System.out.println(c);
		
		
	}
}