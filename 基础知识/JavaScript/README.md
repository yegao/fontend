# JavaScript基础知识

## 数据类型

### 原始值

原始值就是不能更改的值。例如（与C语言不同），字符串是不可变的。我们将这些类型的值称为原始值。

#### Boolean类型

Boolean表示逻辑实体，具有两种值：true和false。

#### Null类型

Null类型只有一个值：null。

#### Undefined类型

Undefined类型只有一个值：undefined，未主动分配值的变量的默认值就是undefined。

#### Number类型

Number类型是双精度64位二进制格式IEEE 754值（负2的53次方减1 到 正2的53次方减1之间的数字）。除了表示浮点数，数字类型还具有三个符号值：+ Infinity，-Infinity和NaN（"非数字"）。要检查±Infinity内的最大可用值或最小可用值，可以使用常数Number.MAX_VALUE或Number.MIN_VALUE。

#### BigInt类型

BigInt类型可以表示任意精度的整数。 使用BigInt，您可以安全地存储和操作大整数，甚至可以超出Numbers的安全整数限制。
可以通过将n附加到整数的末尾或调用构造函数来创建BigInt。

```js
var x1 = 999999999999999n; // typeof x1 === "bigint"
var x2 = BigInt(999999999999999); // typeof x2 === "bigint"
```

#### String类型

String类型用于表示文本数据。它是由一组16位无符号整数值的元素组合而成。第一个元素在索引0处，第二个元素在索引1处，依此类推。字符串的长度是其中的元素个数。
与某些编程语言（例如C）不同，JavaScript字符串是不可变的。这意味着一旦创建了字符串，就无法对其进行修改。但是，仍然可以基于对原始字符串的操作来创建另一个字符串。例如：

* 通过索引或使用`String.substr()`来获取原始字符串的子字符串。
* 使用串联运算符`+`或`String.concat()`对两个字符串进行串联。

#### Symbol类型

Symbol类型的值是唯一且不可变的原始值，可以用作Object属性的键。

### 对象

在计算机科学中，对象是内存中的值，可能由标识符引用。在JavaScript中，对象可以看作是属性的集合。使用`{}`语法，可以初始化一组有限的属性，然后就可以添加和删除属性。属性值可以是任何类型的值，包括其他对象，从而可以构建复杂的数据结构。键值可以是String类型的值或Symbol类型的值。

### 小结

最新的ECMAScript标准定义了7种原始类型，其中6中原始类型可以用typeof运算符检测:

* undefined :  typeof x === "undefined"
* Boolean   :  typeof x === "boolean"
* Number    :  typeof x === "number"
* String    :  typeof x === "string"
* BigInt    :  typeof x === "bigint"
* Symbol    :  typeof x === "symbol"

Null类型是一种特殊的原始类型，typeof x === "object"，如果一个对象没有继承任何其他的对象，则在其原型链的末端会是null。

另外还有一种复杂类型，为Object类型。
