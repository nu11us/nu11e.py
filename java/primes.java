public class primes{
    public static int[] primes(int max){   
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
        int counter = 0;
        int j = 0;
        for(int i=2;i<max; i++){
            if(isPrime[i]){
                counter++;
            }
        }
        int prime[] = new int[counter];
        for(int i=2;i<max; i++){
            if(isPrime[i]){
                prime[j]=i;
                j++;
            }
        }
        return prime;
    }
}
