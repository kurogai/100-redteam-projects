using vie_genere.Parameters;

namespace vie_genere;

/// <summary>
///     Represents the data needed for the <see cref="VigenereService"/>.
/// </summary>
public sealed class VigenereData
{
    /// <summary>
    ///     The input to encrypt or decryt.
    /// </summary>
    public string Input {get;set;}

    /// <summary>
    ///     The key used in the Vigenere cipher.
    /// </summary>
    public char[] Key {get;set;}

    /// <summary>
    ///     The allowed characters to use in the Vigenere cipher.
    /// </summary>
    public char[] Alphabet {get;set;}

    /// <summary>
    ///     Constructor that uses the parameters from the command line.
    /// </summary>
    /// <param name="parametersBase">Parameters from the command line.</param>
    public VigenereData(ParametersBase parametersBase):this(parametersBase.Input, parametersBase.Key, parametersBase.Alphabet){}

    /// <summary>
    ///     Private constructor, check the validity of parameters.
    /// </summary>
    /// <param name="input">Input to encrypt or decrypt.</param>
    /// <param name="key">Key used by the Vigenere cipher.</param>
    /// <param name="alphabet">Allowed characters used by the Vigenere cipher.</param>
    /// <exception cref="ArgumentNullException"></exception>
    /// <exception cref="ArgumentException"></exception>
    /// <exception cref="ArgumentOutOfRangeException"></exception>
    private VigenereData(string input, string key, string alphabet)
    {
        ValidateParameters(input, key, alphabet);

        Input = input;
        Key = key.ToCharArray();
        Alphabet = alphabet.ToCharArray();
    }

    /// <summary>
    ///     Validate the parameters in the coonstructor.
    /// </summary>
    /// <param name="input">Input to encrypt or decrypt.</param>
    /// <param name="key">Key used by the Vigenere cipher.</param>
    /// <param name="alphabet">Allowed characters used by the Vigenere cipher.</param>
    /// <exception cref="ArgumentNullException"></exception>
    /// <exception cref="ArgumentException"></exception>
    /// <exception cref="ArgumentOutOfRangeException"></exception>
    private static void ValidateParameters(string input, string key, string alphabet)
    {
        if (string.IsNullOrEmpty(input))
        {
            throw new ArgumentNullException(nameof(input));
        }
        if (string.IsNullOrEmpty(key))
        {
            throw new ArgumentNullException(nameof(key));
        }
        if (string.IsNullOrEmpty(alphabet))
        {
            throw new ArgumentNullException(nameof(alphabet));
        }
        if (alphabet.Distinct().Count() != alphabet.Length)
        {
            throw new ArgumentException("The alphabet is a set, it must have only distinct characters.", nameof(alphabet));
        }
        if (input.Any(inputCharacter => !alphabet.Contains(inputCharacter) && inputCharacter != ' '))
        {
            throw new ArgumentOutOfRangeException(nameof(input), "The input must be composed only of characters present in alphabet.");
        }
        if (key.Any(keyCharacter => !alphabet.Contains(keyCharacter)))
        {
            throw new ArgumentOutOfRangeException(nameof(key), "The key must be composed only of characters present in alphabet.");
        }
    }
}
