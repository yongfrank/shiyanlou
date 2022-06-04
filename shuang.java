public class shuang {
    public static void main(String[] args) {
        System.out.println("Hi, shuaing ");
        System.out.println("1".getBytes());
        byteToInt("a".getBytes(), 0);
    }

    public static int transform(byte temp) {
        if (temp >= 0) {
            return temp;
        }
        int tempInt = temp + 256;
        return tempInt;
    }
    
    public static int[] byteToInt(byte[] content, int offset) {
        int[] result = new int[content.length >> 2];
        int i = 0;
        for (int j = offset; j < content.length; j += 4) {
            result[i] = transform(content[j + 3]) | (transform(content[j + 2]) << 8) | (transform(content[j + 1]) << 16) | (content[j] << 24);
            i++;
        }
        return result;
    }
}

