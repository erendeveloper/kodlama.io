public class Main {
    public static void main(String[] args) {
        int toplam=topla(1,2,3,4,5);
        System.out.println(toplam);
    }

    public static int topla(int... sayilar){//liste gibi foner
        int toplam=0;
        for(int sayi:sayilar){
            toplam+=sayi;
        }
        return toplam;
    }
}