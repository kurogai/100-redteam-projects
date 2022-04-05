import javax.swing.*;
import javax.swing.border.EmptyBorder;
import javax.swing.event.DocumentEvent;
import javax.swing.event.DocumentListener;
import javax.swing.text.BadLocationException;
import javax.swing.text.NumberFormatter;
import java.text.NumberFormat;

public class Main extends JFrame {
    private final JLabel labelInput, labelOutput, labelOffset;
    private final JScrollPane scrollPaneInput, scrollPaneOutput;
    private final JTextArea textAreaInput, textAreaOutput;
    private final JFormattedTextField jTextFieldOffset;
    private final JToggleButton jToggleButton;
    private int offset = 3;
    private String message = "";

     public Main() {
        JPanel contentPane = new JPanel();
        setTitle("Caesar Cipher tool");
        setResizable(false);
        setBounds(100, 100, 800, 600);
        contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setContentPane(contentPane);
        contentPane.setLayout(null);

        //toggle
         jToggleButton = new JToggleButton("Decrypt");
         jToggleButton.setBounds(90, 5 , 100,20);
         jToggleButton.addActionListener(actionEvent -> {
             if (jToggleButton.isSelected()) {
                 jToggleButton.setText("Encrypt");
                 cipherDecipher(message,offset);
             }
             else {
                 jToggleButton.setText("Decrypt");
                 cipherDecipher(message,offset);
             }
         });
         contentPane.add(jToggleButton);

         //offset
         labelOffset = new JLabel("Offset:");
         labelOffset.setBounds(265, 0 , 146,29);

         NumberFormat longFormat = NumberFormat.getIntegerInstance();
         NumberFormatter numberFormatter = new NumberFormatter(longFormat);
         numberFormatter.setValueClass(Long.class); //optional, ensures you will always get a long value
         numberFormatter.setMinimum(1L); //Optional
         numberFormatter.setMaximum(28L); //Optional

         jTextFieldOffset = new JFormattedTextField(numberFormatter);
         jTextFieldOffset.setBounds(320, 5 , 30,20);
         jTextFieldOffset.setText("3");
         jTextFieldOffset.getDocument().addDocumentListener(new DocumentListener() {
             @Override
             public void insertUpdate(DocumentEvent documentEvent) {
                 offset = Integer.parseInt(jTextFieldOffset.getText());
                 cipherDecipher(message,offset);
             }

             @Override
             public void removeUpdate(DocumentEvent documentEvent) {}

             @Override
             public void changedUpdate(DocumentEvent documentEvent) {
                 offset = Integer.parseInt(jTextFieldOffset.getText());
                 cipherDecipher(message,offset);
             }
         });

         contentPane.add(labelOffset);
         contentPane.add(jTextFieldOffset);

        //input
         labelInput = new JLabel("Input:");
         labelInput.setBounds(10, 0, 146, 29);
         contentPane.add(labelInput);

         scrollPaneInput = new JScrollPane();
         scrollPaneInput.setEnabled(false);
         scrollPaneInput.setBounds(10, 30, 780, 250);

         textAreaInput = new JTextArea();
         textAreaInput.getDocument().addDocumentListener(new DocumentListener() {
             @Override
             public void insertUpdate(DocumentEvent documentEvent) {
                 try {
                     message = documentEvent.getDocument().getText(0, documentEvent.getDocument().getLength());
                     cipherDecipher(message,offset);
                 } catch (BadLocationException e) {
                     e.printStackTrace();
                 }
             }

             @Override
             public void removeUpdate(DocumentEvent documentEvent) {
                 try {
                     message = documentEvent.getDocument().getText(0, documentEvent.getDocument().getLength());
                     cipherDecipher(message,offset);
                 } catch (BadLocationException e) {
                     e.printStackTrace();
                 }

             }

             @Override
             public void changedUpdate(DocumentEvent documentEvent) {
                 try {
                     message = documentEvent.getDocument().getText(0, documentEvent.getDocument().getLength());
                     cipherDecipher(message,offset);
                 } catch (BadLocationException e) {
                     e.printStackTrace();
                 }

             }
         });
         scrollPaneInput.setViewportView(textAreaInput);
         contentPane.add(scrollPaneInput);

         //output
         labelOutput = new JLabel("Output:");
         labelOutput.setBounds(10, 275, 146, 29);

         scrollPaneOutput = new JScrollPane();
         scrollPaneOutput.setEnabled(false);
         scrollPaneOutput.setBounds(10, 300, 780, 250);

         textAreaOutput = new JTextArea();
         scrollPaneOutput.setViewportView(textAreaOutput);

         contentPane.add(labelOutput);
         contentPane.add(scrollPaneOutput);
         scrollPaneOutput.setViewportView(textAreaOutput);
    }

    private void cipherDecipher(String message, int offset){
        if (!jToggleButton.isSelected()) {
            textAreaOutput.setText(cipher(message, offset));
        }
        else{
            textAreaOutput.setText(cipher(message,26 - (offset % 26)));
        }
    }

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

    public static void main(String[] args){
        Main main = new Main();
        main.setVisible(true);
    }
}
