using System.Globalization;
using CommandLine;
using vie_genere;
using vie_genere.Parameters;

internal class Program
{
    private static async Task<int> Main(string[] args)
    {
        var parser = new Parser(with => 
        {
            with.AutoHelp = true;
            with.AutoVersion = true;
            with.CaseInsensitiveEnumValues = false;
            with.CaseSensitive = true;
            with.EnableDashDash = true;
            with.ParsingCulture = CultureInfo.CurrentCulture;
            with.HelpWriter = Console.Out;
        });
        return await parser.ParseArguments<EncryptParameters, DecryptParameters>(args)
            .MapResult(parameters => {
                return Execute((ParametersBase)parameters);
            }, _ => Task.FromResult(1));
    }

    private static Task<int> Execute(ParametersBase parameters)
    {
        var cancellationTokenSource = new CancellationTokenSource();
        string res = string.Empty;
        switch(parameters)
        {
            case EncryptParameters encryptParameters :
                res = VigenereService.Encrypt(new VigenereData(encryptParameters), cancellationTokenSource.Token,
                    parameters.MaxDegreeOfParallelism);
                break;
            
            case DecryptParameters decryptParameters:
                res = VigenereService.Decrypt(new VigenereData(decryptParameters), cancellationTokenSource.Token,
                    parameters.MaxDegreeOfParallelism);
                break;
            
            default:
                throw new ArgumentException("Not valid parameters.", nameof(parameters));
        }
        Console.WriteLine(res);
        return Task.FromResult(0);
    }
}