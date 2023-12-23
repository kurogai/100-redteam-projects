using System.Runtime.CompilerServices;

[assembly: InternalsVisibleTo("vie-genere.Tests")]
namespace vie_genere;

/// <summary>
///     Helper class used to encrypt and decrypt Vigenere Cipher.
/// </summary>
public static class VigenereService
{
    /// <summary>
    ///     Compute the postivie value of modulo (<paramref name="modulo"/>) of a value (<paramref name="val"/>).
    /// </summary>
    /// <param name="val">Source to compute in modulo.</param>
    /// <param name="modulo">Modulo used.</param>
    /// <returns>The value must be <paramref name="val"/> % <paramref name="modulo"/> and positive.</returns>
    /// <exception cref="ArgumentOutOfRangeException"></exception>
    internal static int PositiveMod(int val, int modulo)
    {
        if(modulo <= 0)
        {
            throw new ArgumentOutOfRangeException(nameof(modulo), "Modulo must be strictly positive.");
        }
        int res = val;
        while(res < 0)
        {
            res += modulo;
        }
        return res % modulo;
    }

    /// <summary>
    ///     Encrypt or decrypt the <paramref name="vigenereData"/> in function of <paramref name="useEncrypt"/> parameter.
    /// </summary>
    /// <param name="vigenereData">Contains the input, the key and the alphabet (see <see cref="VigenereData"/>)</param>
    /// <param name="maxDegreeOfParallelism">The degree of parallelism (10 => 10 thread as maximum).</param>
    /// <param name="useEncrypt">If True it encrypts else it decrypts.</param>
    /// <param name="cancellationToken">Token to cancel the parallelization.</param>
    /// <returns>Encrypted or decrypted data.</returns>
    /// <exception cref="ArgumentException"></exception>
    /// <exception cref="ArgumentOutOfRangeException"></exception>
    private static string EncryptOrDecrypt(VigenereData vigenereData, int maxDegreeOfParallelism,
        bool useEncrypt, CancellationToken cancellationToken)
    {
        if(maxDegreeOfParallelism < 0) throw new ArgumentException("The maximum degree of parallelism must be stricly positive.", nameof(maxDegreeOfParallelism));
        var parallelOptions = new ParallelOptions
        {
            CancellationToken = cancellationToken,
            MaxDegreeOfParallelism = maxDegreeOfParallelism
        };
        var words = vigenereData.Input.Split();
        var concatenatedRes = new string[words.Length];
        var offset = 0;
        for(int wordIndex = 0; wordIndex < words.Length; wordIndex++)
        {
            var word = words[wordIndex];
            var res = new char[word.Length];
            Parallel.For(0,
                word.Length,
                parallelOptions,
                (inputIndex, loopstate) => {
                    var currentInputLetter = word[inputIndex];
                    var indexInAlphabet = Array.IndexOf(vigenereData.Alphabet, currentInputLetter);
                    if(indexInAlphabet < 0) throw new ArgumentOutOfRangeException(nameof(vigenereData.Input),
                        "The input must be composed only of characters present in alphabet.");

                    var keyUsed = vigenereData.Key[PositiveMod(inputIndex + offset, vigenereData.Key.Length)];
                    var keyUsedIndexInAlphabet = Array.IndexOf(vigenereData.Alphabet, keyUsed);
                    if(keyUsedIndexInAlphabet < 0) throw new ArgumentOutOfRangeException(nameof(vigenereData.Key),
                        "The key must be composed only of characters present in alphabet.");

                    var outputIndex = useEncrypt ?
                        indexInAlphabet + keyUsedIndexInAlphabet
                        : indexInAlphabet - keyUsedIndexInAlphabet;
                    var outputModuloIndex = PositiveMod(outputIndex, vigenereData.Alphabet.Length);

                    res[inputIndex] = vigenereData.Alphabet[outputModuloIndex];
                    if(loopstate.ShouldExitCurrentIteration) return;
                });
            concatenatedRes[wordIndex] = new string(res);
            offset += word.Length;
        }
        return string.Join(' ', concatenatedRes);
    }

    /// <summary>
    ///     Encrypt the <paramref name="vigenereData"/>.
    /// </summary>
    /// <param name="vigenereData">Contains the input, the key and the alphabet (see <see cref="VigenereData"/>)</param>
    /// <param name="cancellationToken">Token to cancel the parallelization.</param>
    /// <param name="maxDegreeOfParallelism">The degree of parallelism (10 => 10 thread as maximum).</param>
    /// <returns>Encrypted value of <paramref name="input"/></returns>
    public static string Encrypt(VigenereData vigenereData, CancellationToken cancellationToken, int maxDegreeOfParallelism = 10) =>
        EncryptOrDecrypt(vigenereData, maxDegreeOfParallelism, true, cancellationToken);

    /// <summary>
    ///     Decrypt the <paramref name="vigenereData"/>.
    /// </summary>
    /// <param name="vigenereData">Contains the input, the key and the alphabet (see <see cref="VigenereData"/>)</param>
    /// <param name="cancellationToken">Token to cancel the parallelization.</param>
    /// <param name="maxDegreeOfParallelism">The degree of parallelism (10 => 10 thread as maximum).</param>
    /// <returns>Decrypted value of <paramref name="input"/></returns>
    public static string Decrypt(VigenereData vigenereData, CancellationToken cancellationToken, int maxDegreeOfParallelism = 10) =>
        EncryptOrDecrypt(vigenereData, maxDegreeOfParallelism, false, cancellationToken);
}
