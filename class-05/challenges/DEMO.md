# Ops Challenge: File Encryption

## Syntax

```powershell
Get-FileHash [-Path] <String[]> [[-Algorithm] <String>] [<CommonParameters>]
Get-FileHash [-LiteralPath] <String[]> [[-Algorithm] <String>] [<CommonParameters>]
Get-FileHash [-InputStream] <Stream> [[-Algorithm] <String>][<CommonParameters>]
```

## Example Code

**Example 1: Compute the hash value for a file**

This example uses the `Get-FileHash` cmdlet to compute the hash value for the `/etc/apt/sources.list` file. The hash algorithm used is SHA256. The output is piped to the `Format List` cmdlet to format the output as a list.

```powershell
Get-FileHash /etc/apt/sources.list | Format-List

Algorithm : SHA256
Hash      : 3CBCFDDEC145E3382D592266BE193E5BE53443138EE6AB6CA09FF20DF609E268
Path      : /etc/apt/sources.list
```

**Example 2: Compute the hash value for an ISO file**

This example uses the `Get-FileHash` cmdlet and the SHA384 algorithm to compute the hash for an ISO file that an admin has downloaded from the internet. Output is piped to the `Format-List` cmdlet to format the output as a list

```powershell
Get-FileHash C:\Users\user1\Downloads\Contoso8_1_ENT.iso -Algorithm SHA384 | Format-List

Algorithm : SHA384
Hash      : 20AB1C2EE19FC96A7C66E33917D191A24E3CE9DAC99DB7C786ACCE31E559144FEAFC695C58E508E2EBBC9D3C96F21FA3
Path      : C:\Users\user1\Downloads\Contoso8_1_ENT.iso
```

**Example 3: Compute the hash value of a stream**

This example uses the `System.Net.WebClient` to download a package from the Powershell release page. We can compare the published hash value with the one we calculate with `Get-FileHash`

```powershell
$wc = [System.Net.WebClient]::new()
$pkgurl = 'https://github.com/PowerShell/PowerShell/releases/download/v6.2.4/powershell_6.2.4-1.debian.9_amd64.deb'
$publishedHash = '8E28E54D601F0751922DE24632C1E716B4684876255CF82304A9B19E89A9CCAC'
$FileHash = Get-FileHash -InputStream ($wc.OpenRead($pkgurl))
$FileHash.Hash -eq $publishedHash

True
```

**Example 4: Compute the hash of a string**

PowerShell **does not** provide a cmdlet to compute the hash of a string. A workaround is to write a string to a stream and use the `InputStream` parameter of `Get-FileHash` to get the hash value

```powershell
$stringAsStream = [System.IO.MemoryStream]::new()
$writer = [System.IO.StreamWriter]::new($stringAsStream)
$writer.write("Hello world")
$writer.Flush()
$stringAsStream.Position = 0
Get-FileHash -InputStream $stringAsStream | Select-Object Hash

Hash
----
64EC88CA00B268E5BA1A35678A1B5316D212F4F366B2477232534A8AECA37F3C
```

## Demo Code

Here is the code that was demonstrated in class.

```powershell
# Encrypt a file
(Get-Item –Path "C:\Users\administrator\Desktop\filename").Encrypt()

# Decrypt a file
(Get-Item –Path "C:\Users\administrator\Desktop\filename").Decrypt()

# Generate an encrypted string from a plaintext string
"P@ssword1" | ConvertTo-SecureString -AsPlainText -Force | ConvertFrom-SecureString

# Generate a hash without specifying the algorithm
Get-FileHash "C:\Users\administrator\Desktop\filename"

# Specify SHA256 algorithm explicitly
Get-FileHash "C:\Users\administrator\Desktop\filename" -Algorithm SHA256
```
