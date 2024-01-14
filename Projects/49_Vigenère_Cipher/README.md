# Vigenere cipher

This is an implementation of vigenère cipher written in C# .NET 6.0

## :information_source: Technologies used

* C#

## :information_source: How to use?
```bash
# Clone the repository
$ git clone https://github.com/kurogai/100-redteam-projects.git

# Enter the repository
$ cd 100-redteam-projects\Projects\49_Vigenère_Cipher
```

### Using Docker
```bash
# Build the image
docker build -t 'vie-genere' -f Dockerfile .

# Run the image with 'help'
docker run -it --rm 'vie-genere' help
```

### With .NET SDK installed
If .NET SDK is installed, you can build it and run it like the Dockerfile does:  
```bash
# Restore as distinct layers
dotnet restore
# Build and publish a release
dotnet publish -c Release -o out
# Run it
./out/vie-genere help
```

## Developer
<p align="center">
<a href="https://github.com/Eneru" target="blank"><img align="center" src="https://avatars.githubusercontent.com/u/3764440?v=4" alt="Eneru" height="100" width="100" /></a>
</p>