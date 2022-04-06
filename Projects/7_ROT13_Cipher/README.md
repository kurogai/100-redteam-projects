<h1 align="center">ROT13 Cipher tool</h1>

## :information_source:  technologies used

* Java

<h2 align="center"> Encrypt </h2>

![image](https://user-images.githubusercontent.com/32443720/161871552-8069d2bb-5401-47d3-8540-8ef7a8109c96.png)


<h2 align="center"> Decrypt </h2>

![image](https://user-images.githubusercontent.com/32443720/161871561-16ca9506-19e2-49c4-9b81-183ec77a917c.png)


```java
private void cipherDecipher(String message, int offset){
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < message.length(); i++) {
            char c = message.charAt(i);
            if       (c >= 'a' && c <= 'm') c += offset;
            else if  (c >= 'A' && c <= 'M') c += offset;
            else if  (c >= 'n' && c <= 'z') c -= offset;
            else if  (c >= 'N' && c <= 'Z') c -= offset;
            sb.append(c);
        }
        textAreaOutput.setText(sb.toString());
}
```

## :books: References

https://stackoverflow.com/questions/25537465/rot13-decode-in-java

https://en.wikipedia.org/wiki/ROT13