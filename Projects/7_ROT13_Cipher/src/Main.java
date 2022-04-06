import javax.swing.*;
import javax.swing.border.EmptyBorder;
import javax.swing.event.DocumentEvent;
import javax.swing.event.DocumentListener;
import javax.swing.text.BadLocationException;

public class Main extends JFrame {
    private final JTextArea textAreaOutput;
    private final int offset = 13;
    private String message = "";

     public Main() {
        JPanel contentPane = new JPanel();
        setTitle("ROT13 Cipher tool");
        setResizable(false);
        setBounds(100, 100, 800, 600);
        contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setContentPane(contentPane);
        contentPane.setLayout(null);

        //input
         JLabel labelInput = new JLabel("Input:");
         labelInput.setBounds(10, 0, 146, 29);
         contentPane.add(labelInput);

         JScrollPane scrollPaneInput = new JScrollPane();
         scrollPaneInput.setEnabled(false);
         scrollPaneInput.setBounds(10, 30, 780, 250);

         JTextArea textAreaInput = new JTextArea();
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
         JLabel labelOutput = new JLabel("Output:");
         labelOutput.setBounds(10, 275, 146, 29);

         JScrollPane scrollPaneOutput = new JScrollPane();
         scrollPaneOutput.setEnabled(false);
         scrollPaneOutput.setBounds(10, 300, 780, 250);

         textAreaOutput = new JTextArea();
         scrollPaneOutput.setViewportView(textAreaOutput);

         contentPane.add(labelOutput);
         contentPane.add(scrollPaneOutput);
         scrollPaneOutput.setViewportView(textAreaOutput);
    }

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

    public static void main(String[] args){
        Main main = new Main();
        main.setVisible(true);
    }
}
