<h1 align="center">Caesar Cipher tool</h1>

## :information_source:  technologies used

* Java

<h2 align="center"> Encrypt </h2>

![image](https://user-images.githubusercontent.com/32443720/161679424-cc0fc73f-2837-4ece-b8a0-5faec3cb016b.png)

<h2 align="center"> Decrypt </h2>

![image](https://user-images.githubusercontent.com/32443720/161679536-6b60c399-3a74-49b1-9788-7c6b52155ded.png)



```java
private String cipher(String message, int offset) {
    StringBuilder result = new StringBuilder();
    for (char character : message.toCharArray()) {
        if (character != ' ') {
            int originalAlphabetPosition = character - 'a';
            int newAlphabetPosition = (originalAlphabetPosition + offset) % 26;
            char newCharacter = (char) ('a' + newAlphabetPosition);
            result.append(newCharacter);
        } else {
            result.append(character);
        }
    }
    return result.toString();
}
```

## :books: References

https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/