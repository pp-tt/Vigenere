# Vigenere
多表代换Virginia加密算法及秘钥破解算法的实现：编程语言为C语言或其它语言，要求提交加密、解密、破解源代码文件。实现对任意有意义的英文文本文件（*.txt）的Virginia加密、解密算法，其中秘钥是任意输入的一个字符串。要求提供明文文本文件、密文文本文件。在不知道秘钥的情况下，对一个用Virginia加密算法生成的密文文本文件进行破解，包括破解秘钥、生成对应的明文。要求提供程序测试说明文档。

下载后直接运行`main.py`文件即可，运行后在当前目录生成 KEY 文件和 加密文件，以及解密文件，`原始文件.txt`为有意义的英文字符，文件内容如下:

> Differential Privacy is the state-of-the-art goal for the problem of privacy-preserving data release and privacy-preserving data mining.Existing techniques using differential privacy,however,cannot effectively handle the publication of high-dimensional data.In particular,when the input dataset contains a large number of attributes,existing methods incur higher computing complexity and lower information to noise ratio,which renders the published data next to useless.This proposa aims to reduce computing complexity and signal to noise ratio.The starting point is to approximate the full distribution of high-dimensional dataset with a set of low-dimensional marginaldistributions via optimizing score function and reducing sensitivity,in which generation of noisy conditional distributions with differential privacy is computed in a set of low-dimensional subspaces,and then,the sample tuples from the noisy approximation distribution are used to generate and release the synthetic dataset.Some crucial science problems would be investigated below:(i)constructing a low k-degree Bayesian network over the high-dimensional dataset via exponential mechanism in differential privacy,where the score function is optimized to reduce the sensitivity using mutual information,equivalence classes in maximum joint distribution and dynamic programming;(ii)studying the algorithm to compute a set of noisy conditional distributions from joint distributions in the subspace of Bayesian network,via the Laplace mechanism of differential privacy.(iii)exploring how to generate synthetic data from thedifferentially private Bayesian network and conditional distributions,without explicitly materializing the noisy global distribution.The proposed solution may have theoretical and technical significance for synthetic data generation with differential privacy on business prospects.

启动程序如下：

```python
if __name__ == "__main__":
    cipher = encryption('./原始文件.txt', './加密文件.txt', 'hello')
    key = get_key('./加密文件.txt', 'KEY.txt')
    decrypt('./加密文件.txt', './解密结果.txt', key)
```

