public class Main {
    public static void main(String[] args) {
        char harf='E';

        switch (harf){
            case 'A':
            case 'I':
            case 'O':
            case 'U':
                System.out.println("Kalin sesli harfl");
                break;
            default:
                System.out.println("ince sesli harfl");
        }
    }
}