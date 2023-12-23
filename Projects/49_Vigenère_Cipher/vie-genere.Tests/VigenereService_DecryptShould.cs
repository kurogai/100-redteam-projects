using vie_genere.Parameters;

namespace vie_genere.Tests;
public class VigenereService_DecryptShould
{
    [Theory]
    [InlineData("C", "B", "AB")]
    [InlineData("A", "C", "AB")]
    public void Decrypt_InputOrKeyNotInAlphabet_ThrowArgumentOutOfRangeException(string input, string key, string alphabet)
    {
        // Arrange
        var maxDegreeOfParallelism = 10;
        var cancellationToken = new CancellationTokenSource().Token;
        var vigenereData = new VigenereData(new DecryptParameters
        {
            Alphabet = alphabet,
            Input = "A",
            Key = "B",
            MaxDegreeOfParallelism = maxDegreeOfParallelism
        })
        {
            Input = input,
            Key = key.ToCharArray()
        };

        // Act
        // Assert
        Assert.Throws<AggregateException>(() => VigenereService.Decrypt(vigenereData, cancellationToken, maxDegreeOfParallelism));
    }

    [Fact]
    public void Decrypt_ValidInput_ReturnOutputOfSameLength()
    {
        // Arrange
        var vigenereData = new VigenereData(new DecryptParameters
            {
                Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                Input = "DLGC MQ K XCCX QORRORAO",
                Key = "KEY",
                MaxDegreeOfParallelism = 10
            });
        var expected = "THIS IS A TEST SENTENCE";

        // Act
        var result = VigenereService.Decrypt(vigenereData,
            new CancellationTokenSource().Token);

        // Assert
        Assert.NotEqual(vigenereData.Input, result);
        Assert.Equal(vigenereData.Input.Length, result.Length);
        Assert.Equal(expected, result);
    }
}
