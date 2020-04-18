# JavaScript

## 数据类型

### 不可变的原始值和可变的对象引用

JavaScript中的原始值（undefined、null、布尔值、数字、字符串）与对象（包括数组和函数）有着根本的区别。原始值是不可更改的：任何方法都无法更改（或者突变）一个原始值。对数字和布尔值来说显然如此（改变数字的值本身就说不通），而对字符串来说就不那么明显了，因为字符串看起来像由字符组成的数组，我们期望可以通过指定索引来修改字符串中的字符。实际上，JavaScript是禁止这样做的。字符串中所有的方法看上去返回了一个修改后的字符串，实际上返回的是一个新的字符串值。

```js
var s = "hello"; // 定义一个由消协字母组成的文本
s.toUpperCase(); // 返回"HELLO"，但并没有改变s的值
s                // => "hello"，原始字符串的值并没有被改变
```

原始值的比较是值的比较：只有在他们的值相等的时候他们才相等。

```js
var x = 2;
var y = 2;
x === y; // true
```

对象和原始值不同，对象是可变的（它们的值是可修改的）。

```js
var o = { x: 1 };    // 定义一个对象
o.x = 2;             // 通过修改对象属性值来更改对象
o.y = 3;             // 再次更改这个对象，给他们增加一个新属性
```

对象的比较并非值的比较（即使两个对象包含相同的属性和相同的值，它们也是不想等的，各个索引完全相等的两个数组也是不相等的）。我们通常将对象称为引用类型，以此来和JavaScript的基本类型区分开来。依照术语的叫法，对象值都是引用，对象的比较均是引用的比较（当且仅当他们引用同一个基对象的时候，它们才相等）。

```js
var o1 = {};
var o2 = {};
o1 === o2; // false
```

```js
var o1 = {};
var o2 = o1;
o2.x = 2;
o1 === o2; // true
```

#### 布尔类型

Boolean表示逻辑实体，具有两种值：true和false。

#### null和undefined

null用于描述一个“空值”，对null执行typeof运算，会得到"object"。
undefined表示值的空缺，用未定义的值表示更深层次的“空值”。它是变量的一种取值，表示变量没有初始化。

* 如果查询对象的属性或则数组元素的值时返回undefined，则表示这个属性或者元素不存在。
* 如果函数没有返回任何值，则返回undefined。
* 引用没有提供实参的函数形参也只会得到undefined。

undefined一开始的时候是一个预定义的全局变量（它和null不一样，它不是一个关键字），它的值就是“未定义”。在ECMAScript3中，undefined是可读/写的变量，可以给它赋任意的值。这个错误在ECMAScript5中做了修正，undefined在该版本中是只读的。如果使用typeof运算符得到undefined的类型，则返回"undefined"，表明这个值是这个类型的唯一成员。

尽管null和undefined是不同的，但是它们都表示“值的空缺”，两者往往可以互换。判断相等运算符“==”认为两者是相等的（所以我们需要要使用“===”严格相等运算符来区分他们）。

```js
null == undefined; //true
null === undefined; // false
```

> 个人做法：一般我在实际项目中，我会将undefined作为系统级、出乎意料的或者类似错误的值的空缺，而null是表示程序级，正常的或者是在意料之中的值的空缺。如果想将它们赋值给变量或者属性，或者将它们作为参数传入函数，最佳选择是使用null。

#### 数字类型

数字类型是双精度64位二进制格式IEEE 754值（负2的53次方减1 到 正2的53次方减1之间的数字）。除了表示浮点数，数字类型还具有三个符号值：+ Infinity，-Infinity和NaN（"非数字"）。要检查±Infinity内的最大可用值或最小可用值，可以使用常数Number.MAX_VALUE或Number.MIN_VALUE。

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

### 包装对象

观察以下下面字符串的用法

```js
var s = "hello world";
var world = s.substring(6, s.length);
```

我们前面说了，字符串类型是原始类型，不是对象，但是它为什么可以和对象一样有属性呢（比如上面例子中的substring、length）？这是因为只要引用了字符串s的属性，JavaScript就会将字符串值通过调用new String(s)的方式转化成对象，这个对象继承了字符串的方法，并被用来处理属性的引用。一旦属性引用结束，这个新创建的对象就会销毁（其实在实现上并不一定创建或者销毁这个临时对象，然而整个过程看起来就是这样）。
同字符串一样，数字和布尔值也具有各自的方法（通过Number()和Boolean()构造函数创建一个临时对象，这些方法的调用均是来自于这个临时对象）。

```js
4.toFloat(); // Uncaught SyntaxError: Invalid or unexpected token 报错是因为JavaScript将这里的点当作小数点了
4..toFloat(); // 4
(-2.4).abs(); // 2.4
```

null和undefined没有包装对象，访问它们的属性的时候会造成一个类型错误。

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

## 变量

### 变量的作用域

一个变量的作用域是程序源代码中定义这个变量的区域，全局变量拥有全局作用域，在ECMAScript 6 之前，JavaScript没有块级作用域，但是有函数作用域，在ECMAScript 6 中，新增了let、const的用法，使用let、const定义的变量属于块级作用域。

#### 全局作用域

如果在声明变量的时候没有使用var、let、const等，那么声明的将是一个全局变量。或者声明变量的时候没有使用函数包裹，该变量也是全局变量。全局变量可以被任何其他代码所访问。

#### 函数作用域

在函数内部使用var声明的变量只能在*该函数*的内部可见。

```txt
---注释---
该函数：指包裹着这个变量且离该变量最近的函数。
```

#### 块级作用域

在一些类似C语言的编程语言中，花括号内的每一段代码都有各自的作用域，变量在声明他们的代码段之外是不可见的，我们称之为块级作用域。
ECMAScript 6 中使用let、const定义的变量属于块级作用域。

```js
if (true) {
  let x = 5;
}
console.log(x); // ReferenceError: x is not defined
```

### 作用域链

JavaScript是基于词法作用域的语言，通过阅读包含变量定义在内的数行源码就可以知道变量的作用域。全局变量在程序中始终都是有定义的，局部变量在声明它的函数体内以及其所嵌套的函数内是有定义的。

如果将一个局部变量看成是一个对象的属性的话，那么可以换个角度区解读变量作用域。在每段JavaScript代码（全局代码或者函数）都有一个与之关联的作用域链（scope chain）。这个作用域链是一个对象列表或者链表，这组对象定义了这段代码对应的作用域中的变量。当JavaScript需要查找变量x的值的时候（这个过程称之为“变量解析”），它会从链中的第一个对象开始查找，如果这个对象中有一个名为x的属性，则会直接使用这个属性的值，如果第一个对象中不存在名为x的属性，则继续查找下一个对象，以此类推。如果作用域链上没有任何一个对象含有属性x，那么就认为这段代码的作用域链上不存在x，并最终跑出一个引用错误异常（ReferenceError）。

* 在JavaScript最顶层的代码中（也就是不包含在任何函数定义内的代码），作用域链由一个全局对象组成。
* 在不包含嵌套函数的函数体内，作用域链上有两个对象，第一个是定义函数参数和局部变量的对象，第二个是全局对象。
* 在一个嵌套的函数体内，作用域链上至少有三个对象。

#### 作用域链的创建规则

当定义一个函数的时候，实际上保存了一个作用域链，当调用这个函数的时候，JavaScript会创建一个存储了这个函数的局部变量的对象，并将这个对象添加到那个作用域链上。对于嵌套函数来讲，每次调用外部函数的时候，内部函数又会重新定义一遍，因为每次调用外部函数的时候，作用域链都是不同的。

## 函数

### 函数声明和函数表达式

### 函数提升

### 函数作用域链

### 闭包

#### 术语来源

闭包这个术语非常古老，它是指函数变量可以被隐藏于作用域之内，看起来就像是函数将变量包裹了起来。

#### 本质

JavaScript采用了词法作用域，函数的执行依赖于变量的作用域，这个作用域是在函数定义的时候就决定了的。JavaScript函数对象的内部状态不仅包含函数的代码逻辑，还必须引用当前的作用域链。函数对象可以通过作用域链相互关联，函数体内部的变量都可以保存在函数作用域内，这种特性在计算机科学中称之为`闭包`。
当调用函数的时候定闭包所指向的作用域链和定义函数的时候闭包所指向的作用域链不同的时候事情就变得很微妙。

很多人认为函数在执行结束之后，与之相关的作用域链似乎也不存在了，但是其实在JavaScript中并非如此。如果一个函数的局部变量定义在CPU的栈中，那么当函数返回时他们的确就不存在了。但是作用域链其实是一个对象列表，不是绑定的栈。每次调用JavaScript函数的时候，都会为之创建一个新的对象用来保存局部变量，然后把这个对象添加到作用域链中。当函数返回的时候，就从作用域链中将这个绑定变量的对象删除。

* 如果不存在嵌套的函数，也没有其他引用指向这个绑定对象，它就会被当作垃圾回收掉。
* 如果定义了嵌套的函数，每个嵌套的函数都各自对应一个作用域链。并且这个作用域链指向一个变量绑定对象。
  * 如果这些嵌套的函数对象在外部函数中保存下来，那么它们也会和所指向的变量绑定对象一样被当作垃圾回收。

  ```js
  function outer(){
    var x = "x"
    function inner(){
      console.log(x);
    }
  }
  ```

  * 如果这个函数定义了嵌套的函数，并且将它作为返回值返回或者存放在某个属性里面，这时候就会有一个外部引用指向这嵌套的函数。它就不会被当作垃圾回收，并且它所指向的变量绑定对象也不会被当作垃圾回收。

  ```js
  function outer(){
    var x = "x"
    function inner(){
      console.log(x);
    }
    return inner;
  }
  /* 测试 */
  var foo = outer();
  foo(); // "x"
  ```

  ```js
  var o = {};
  function outer(){
    var x = "x"
    function inner(){
      console.log(x);
    }
    o.inner = inner;
  }
  /* 测试 */
  o.inner(); // "x"
  ```

### 迭代器协议和可迭代协议

迭代器协议定义了一种标准的方式来产生一个`有限或无限序列的值`，并且当所有的值都已经被迭代后，就会有一个默认的返回值。当一个对象满足下述条件就会被认为是一个`迭代器`：

  1. 它实现了一个`next()`的方法，该方法返回一个对象，该对象必须要有`done`和`value`这两个属性。
  2. 如果`迭代器`已经超过了可迭代次数，值为`true`,这种情况下,`value`的值可以被省略。  
  3. 如果`迭代器`可以产生序列中的下一个值，则为`false`,这种情况下,可以`done`的值可以被省略。

  ```js
  var myIterator = {
      next: function() {
          // ...
          // return {
          //   done: ...
          //   value: ...
          // }
      }
  }
  ```

可迭代协议允许JS对象去定义它们的迭代行为, 例如在一个`for..of`结构中什么值可以被循环。一些内置类型都是内置的可迭代类型并且有默认的迭代行为, 比如`Array`、`Map`等, 另一些类型则不是 (比如普通的`Object`)。可迭代协议就是对象的[Symbol.iterator]是一个无参函数，该函数返回一个`迭代器`(Iterator)。

### 可迭代对象

满足`可迭代协议`的对象就是`可迭代对象`。（）

```js
var o = {
    [Symbol.iterator]: function() {
      return {
        next: function() {
          // ...
          // return {
          //   done: ...
          //   value: ...
          // }
        }
      }
    }
}
```

为了变成可迭代对象， 该对象必须实现`@@iterator`方法, 即必须有一个名字是`Symbol.iterator`的属性。当可迭代对象在被迭代的时候（比如要用于`for..of`中），它的`@@iterator`方法将被调用，然后返回一个用于在迭代中获得值的`迭代器`。

`Array`、`Map`、`Set`、`String`、`TypedArray`等类型的对象、`函数的arguments对象`、`NodeList对象`都是可迭代的对象

`for...of`会获取可迭代对象的`[Symbol.iterator]()`执行的结果，对该`迭代器`逐次调用`next()`，直到`迭代器`返回对象的`done`属性为`true`时，遍历结束。

这里手写一个迭代器

```js
var it = createIterator(["a", "b"]);
it.next(); // { value: "a", done: false }
it.next(); // { value: "b", done: false }
it.next(); // { value: undefined, done: true }
function createIterator(arr) {
  var index = 0;
  return {
    next: function() {
      return index < arr.length
        ? { value: arr[index++], done: false }
        : { value: undefined, done: true };
    },
  };
}
```

更进一步，手写一个迭代器，并使之可迭代

```js
function createIterator(array) {
  var nextIndex = 0;
  return {
    next: function() {
      return nextIndex < array.length
        ? { value: array[nextIndex++], done: false }
        : { value: undefined, done: true };
    },
    [Symbol.iterator]: function () {
        return this // 注意这里是对象调用模式，this指向的就是上层的对象，`迭代器`
    }
  };
}

var iterator = createIterator([1, 2, 3]);
console.log(...iterator);
```

手动创建`迭代器`比较麻烦，所以ES6推出生成器函数语法糖`function*`，方便创建`迭代器`。

```js
function *fn(){
  yield 1
  yield 2
  yield 3
};

var foo = fn();
// foo满足`迭代器协议`，是`迭代器`
foo.next();     // {value: 1, done: false}
foo.next();     // {value: 2, done: false}
foo.next();     // {value: 3, done: false}
foo.next();     // {value: undefined, done: true}
// foo[Symbol.iterator]是一个无参函数，该函数执行后返回生成器对象本身（是`迭代器`），所以是`可迭代对象`
foo[Symbol.iterator]() === foo;   // true
// 可以被迭代
var foo1 = fn()
[...foo1]   // [1, 2, 3]
```

如果在生成器中return一个值，此时会将`done`置为`true`，value就会编程return的那个值时迭代即结束。

```js
function *fn() {
  yield 1;
  return 42;
  yield 2;
}

let foo1 = fn();
foo1.next();           // {value: 1, done: false}
foo1.next();           // {value: 42, done: true}
foo1.next();           // {value: undefined, done: true}

let foo2 = fn();
console.log(...foo2);  // 1
```

另外关于生成器还有另外一种用法，叫生成器委托（yield*）

```js
function* g1() {
  yield 1;
  yield 2;
}

function* g2() {
  yield* g1();      // 委托给g1
  yield* [3, 4];    // 委托给[3, 4]
  yield* "56";      // 委托给"56"
  yield* arguments; // 委托给arguments
}

var generator = g2(7, 8);
console.log(...generator);   // 1 2 3 4 "5" "6" 7 8
```
