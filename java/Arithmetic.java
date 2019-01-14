import java.util.*;

public class Arithmetic{
    public static ArrayList<Integer> primes_erat(int max){
        boolean isPrime[] = new boolean[max+1];
        for(int i=0;i<=max; i++){
            isPrime[i] = true;
        }
        for(int num=2;num<=max; num++){
            if(isPrime[num]){
                for(int n=num*2;n<=max;n+=num){
                    isPrime[n] = false;
                }
            }
        }
        ArrayList<Integer> primes_list = new ArrayList<Integer>();
        for(int i=2;i<max; i++){
            if(isPrime[i]){
                primes_list.add(i);
            }
        }
        return primes_list;
    }
    public static int factorial(int n){
        if (x==0){
            return 1;
        }
        else {
            return x*factorial(x-1);
        }
    }
    public static int nCr(int n, int r){
        return factorial(n) / (factorial(r)*factorial(n-r));
    }
    public static int nPr(int n, int r){
        return factorial(n)/factorial(n-r);
    }
    public static int coll(int n){
        if(n==1){
            return 0;
        }
        else{
            if (x%2==0){
                return 1 + coll(x/2);
            }
            else {
                return 1 + coll(3*x + 1);
            }
        }
    }
    public static ArrayList<Integer> pf(int n){
        ArrayList<Integer> pr = primes(n);
        ArrayList<Integer> newlist = new ArrayList<Integer>();
        for (int i=0; i<pr.size(); i++){
            if (n%pr.get(i)==0){
                newlist.add(pr.get(i));
                newlist.addAll(pf(n/pr.get(i)));
                return newlist;
            }
        }
        newlist.add(n);
        return newlist;
    }
    public static ArrayList<Integer> factors(int n){
        ArrayList<Integer> lst = new ArrayList<Integer>();
        for(int i=1; i<1 + n/2; i++){
            if (n%i==0){
                lst.add(i);
                lst.add(n/i);
            }
        }
        return lst;
    }
}