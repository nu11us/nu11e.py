public class Arithmetic{
    public static ArrayList<Integer> primes(int max){
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
}