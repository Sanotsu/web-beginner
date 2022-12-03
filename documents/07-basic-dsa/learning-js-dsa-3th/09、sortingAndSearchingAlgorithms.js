const Compare = {
    LESS_THAN: -1,
    BIGGER_THAN: 1,
    EQUALS: 0,
};

// 不存在常量
const DOES_NOT_EXIST = -1;

// 默认的比较方法
function defaultCompare(a, b) {
    if (a === b) {
        return Compare.EQUALS;
    }
    return a < b ? Compare.LESS_THAN : Compare.BIGGER_THAN;
}

// 相等判断
function defaultEquals(a, b) {
    return a === b;
}

// 数组内指定索引两个数的交换
function swap(array, a, b) {
    [array[a], array[b]] = [array[b], array[a]];
}


// 模拟未排序的数组
// 要把[5,4,3,2,1]排序成[1,2,3,4,5]
function createNonSortedArray() {
    var array = [];
    for (let i = 5; i > 0; i--) {
        array.push(i);
    }
    return array;
}

// 小于等于方法
function lesserEquals(a, b, compareFn) {
    const comp = compareFn(a, b);
    return comp === Compare.LESS_THAN || comp === Compare.EQUALS;
}
// 大于等于方法
function biggerEquals(a, b, compareFn) {
    const comp = compareFn(a, b);
    return comp === Compare.BIGGER_THAN || comp === Compare.EQUALS;
}

// 求数值的差值方法
function defaultDiff(a, b) {
    return Number(a) - Number(b);
}

// ----------------------------

function bubbleSort(array, compareFn = defaultCompare) {
    // 声明一个名为 length 的变量，用来存储数组的长度
    const { length } = array;
    //   外循环会从数组的第一位迭代至最后一位，它控制了在数组中经过多少轮排序
    for (let i = 0; i < length; i++) {
        // 内循环将从第一位迭代至倒数第二位
        for (let j = 0; j < length - 1; j++) {
            // 进行当前项和下一项的比较
            if (compareFn(array[j], array[j + 1]) === Compare.BIGGER_THAN) {
                // 如果这两项顺序不对（当前项比下一项大），则交换它们
                swap(array, j, j + 1);
            }
        }
    }
    return array;
}


let arr = createNonSortedArray();
console.log(arr);
const array = bubbleSort(arr);
console.log(array);

// ---------------

function modifiedBubbleSort(array, compareFn = defaultCompare) {
    const { length } = array;
    for (let i = 0; i < length; i++) {
        // 从内循环减去外循环中已跑过的轮数，就可以避免内循环中所有不必要的比较
        for (let j = 0; j < length - 1 - i; j++) {
            if (compareFn(array[j], array[j + 1]) === Compare.BIGGER_THAN) {
                swap(array, j, j + 1);
            }
        }
    }
    return array;
}

const array2 = modifiedBubbleSort(arr);
console.log(array2);

// ---------------

const selectionSort = (array, compareFn = defaultCompare) => {
    const { length } = array;
    let indexMin;
    for (let i = 0; i < length - 1; i++) {
        indexMin = i;
        // console.log('index ' + array[i]);
        for (let j = i; j < length; j++) {
            if (compareFn(array[indexMin], array[j]) === Compare.BIGGER_THAN) {
                // console.log('new index min ' + array[j]);
                indexMin = j;
            }
        }
        if (i !== indexMin) {
            swap(array, i, indexMin);
        }
    }
    return array;
};

let array3 = createNonSortedArray(5);
console.log(array3.join());
array3 = selectionSort(array3);
console.log(array3.join());

// ------------------


const insertionSort = (array, compareFn = defaultCompare) => {
    const { length } = array;
    let temp;
    for (let i = 1; i < length; i++) {
        let j = i;
        temp = array[i];
        // console.log('to be inserted ' + temp);
        while (j > 0 && compareFn(array[j - 1], temp) === Compare.BIGGER_THAN) {
            // console.log('shift ' + array[j - 1]);
            array[j] = array[j - 1];
            j--;
        }
        // console.log('insert ' + temp);
        array[j] = temp;
    }
    return array;
};

const array4 = insertionSort(createNonSortedArray());
console.log(array4);

// ---------------------

function merge(left, right, compareFn) {
    let i = 0;
    let j = 0;
    const result = [];
    while (i < left.length && j < right.length) {
        result.push(compareFn(left[i], right[j]) === Compare.LESS_THAN ? left[i++] : right[j++]);
    }
    return result.concat(i < left.length ? left.slice(i) : right.slice(j));
}
function mergeSort(array, compareFn = defaultCompare) {
    if (array.length > 1) {
        const { length } = array;
        const middle = Math.floor(length / 2);
        const left = mergeSort(array.slice(0, middle), compareFn);
        const right = mergeSort(array.slice(middle, length), compareFn);
        array = merge(left, right, compareFn);
    }
    return array;
}

const array5 = mergeSort(createNonSortedArray());
console.log(array5);

// -------------------------------

function partition(array, left, right, compareFn) {
    const pivot = array[Math.floor((right + left) / 2)];
    let i = left;
    let j = right;

    while (i <= j) {
        while (compareFn(array[i], pivot) === Compare.LESS_THAN) {
            i++;
        }
        while (compareFn(array[j], pivot) === Compare.BIGGER_THAN) {
            j--;
        }
        if (i <= j) {
            swap(array, i, j);
            i++;
            j--;
        }
    }
    return i;
}
function quick(array, left, right, compareFn) {
    let index;
    if (array.length > 1) {
        index = partition(array, left, right, compareFn);
        if (left < index - 1) {
            quick(array, left, index - 1, compareFn);
        }
        if (index < right) {
            quick(array, index, right, compareFn);
        }
    }
    return array;
}

function quickSort(array, compareFn = defaultCompare) {
    return quick(array, 0, array.length - 1, compareFn);
}

console.log(quickSort([3, 5, 1, 6, 4, 7, 2]))

// ------------------------
function findMaxValue(array, compareFn = defaultCompare) {
    if (array && array.length > 0) {
        let max = array[0];
        for (let i = 1; i < array.length; i++) {
            if (compareFn(max, array[i]) === Compare.LESS_THAN) {
                max = array[i];
            }
        }
        return max;
    }
    return undefined;
}
function findMinValue(array, compareFn = defaultCompare) {
    if (array && array.length > 0) {
        let min = array[0];
        for (let i = 1; i < array.length; i++) {
            if (compareFn(min, array[i]) === Compare.BIGGER_THAN) {
                min = array[i];
            }
        }
        return min;
    }
    return undefined;
}

function countingSort(array) {
    if (array.length < 2) {
        return array;
    }
    const maxValue = findMaxValue(array);
    let sortedIndex = 0;
    const counts = new Array(maxValue + 1);
    array.forEach(element => {
        if (!counts[element]) {
            counts[element] = 0;
        }
        counts[element]++;
    });
    // console.log('Frequencies: ' + counts.join());
    counts.forEach((element, i) => {
        while (element > 0) {
            array[sortedIndex++] = i;
            element--;
        }
    });
    return array;
}

console.log(countingSort([5, 4, 3, 2, 3, 1]))

// ------------------
function createBuckets(array, bucketSize) {
    let minValue = array[0];
    let maxValue = array[0];
    for (let i = 1; i < array.length; i++) {
        if (array[i] < minValue) {
            minValue = array[i];
        } else if (array[i] > maxValue) {
            maxValue = array[i];
        }
    }
    const bucketCount = Math.floor((maxValue - minValue) / bucketSize) + 1;
    const buckets = [];
    for (let i = 0; i < bucketCount; i++) {
        buckets[i] = [];
    }
    for (let i = 0; i < array.length; i++) {
        buckets[Math.floor((array[i] - minValue) / bucketSize)].push(array[i]);
    }
    return buckets;
}
function sortBuckets(buckets) {
    const sortedArray = [];
    for (let i = 0; i < buckets.length; i++) {
        if (buckets[i] != null) {
            insertionSort(buckets[i]);
            sortedArray.push(...buckets[i]);
        }
    }
    return sortedArray;
}

// 桶排序算法
function bucketSort(array, bucketSize = 5) {
    if (array.length < 2) {
        return array;
    }
    const buckets = createBuckets(array, bucketSize);
    return sortBuckets(buckets);
}

console.log(bucketSort([5, 4, 3, 2, 3, 1]))

// --------------------------
// 获取数的有效位的函数
const getBucketIndex = (value, minValue, significantDigit, radixBase) =>
    Math.floor(((value - minValue) / significantDigit) % radixBase);

// 基数排序算法
function radixSort(array, radixBase = 10) {
    if (array.length < 2) {
        return array;
    }
    const minValue = findMinValue(array);
    const maxValue = findMaxValue(array);

    // 从最后一位开始排序所有的数
    let significantDigit = 1;
    // 如果数组中包含的值都在 1～9，此循环只会执行一次
    // 如果值都小于 99，则循环会执行第二次，以此类推
    while ((maxValue - minValue) / significantDigit >= 1) {
        // console.log('radix sort for digit ' + significantDigit);
        array = countingSortForRadix(array, radixBase, significantDigit, minValue);
        // console.log(array.join());
        // 首先只会基于最后一位有效位对数字进行排序，
        // 在下次迭代时，我们会基于第二个有效位进行排序（十位数字），
        // 然后是第三个有效位（百位数字），以此类推
        significantDigit *= radixBase;
    }
    return array;
}

// 来基于有效位（基数）排序
const countingSortForRadix = (array, radixBase, significantDigit, minValue) => {
    let bucketsIndex;
    const buckets = [];
    const aux = [];
    // 首先，我们基于基数初始化桶
    //   由于我们排序的是十进制数，那么需要 10 个桶。
    for (let i = 0; i < radixBase; i++) {
        buckets[i] = 0;
    }

    //  然后，我们会基于数组中 数的有效位 进行计数排序
    for (let i = 0; i < array.length; i++) {
        // 数的有效位
        bucketsIndex = getBucketIndex(
            array[i],
            minValue,
            significantDigit,
            radixBase
        );
        // 计数排序
        buckets[bucketsIndex]++;
    }
    //  由于我们进行的是计数排序，我们还需要计算累积结果来得到正确的计数值
    for (let i = 1; i < radixBase; i++) {
        buckets[i] += buckets[i - 1];
    }

    // 在计数完成后，要开始将值移回原始数组中。我们会使用一个临时数组（ aux ）来帮助我们
    //   对原始数组中的每个值，我们会再次获取它的有效位并将它的值移动到aux 数组中（从 buckets 数组中减去它的计数值）
    for (let i = array.length - 1; i >= 0; i--) {
        bucketsIndex = getBucketIndex(
            array[i],
            minValue,
            significantDigit,
            radixBase
        );
        aux[--buckets[bucketsIndex]] = array[i];
    }

    // 最后一步是可选的，我们将 aux 数组中的每个值转移到原始数组中。
    // 除了返回 array 之外，我们还可以直接返回 aux数组而不需要复制它的值。
    for (let i = 0; i < array.length; i++) {
        array[i] = aux[i];
    }

    return array;
};

console.log(radixSort([4, 7, 1, 2, 3, 9]))

// ============================
function binarySearch(array, value, compareFn = defaultCompare) {
    // 开始前需要先将数组排序，这里选择了快速排序。
    const sortedArray = quickSort(array);
    // 在数组排序之后，我们设置 low 和 high 指针（它们是边界）
    let low = 0;
    let high = sortedArray.length - 1;

    // 当 low 比 high 小时
    while (low <= high) {
        // 计算得到中间项索引并取得中间项的值
        const mid = Math.floor((low + high) / 2);
        const element = sortedArray[mid];
        // console.log('mid element is ' + element);

        // 接着，我们比较选中项的值和搜索值
        //      如果小了，则选择数组低半边并重新开始
        //      如果选中项的值比搜索值大了，则选择数组高半边并重新开始
        //      若两者都是不是，则意味着选中项的值和搜索值相等，因此直接返回该索引
        if (compareFn(element, value) === Compare.LESS_THAN) {
            low = mid + 1;
            // console.log('low is ' + low);
        } else if (compareFn(element, value) === Compare.BIGGER_THAN) {
            high = mid - 1;
            // console.log('high is ' + high);
        } else {
            // console.log('found it');
            return mid;
        }
    }

    // 此处如果 low比 high 大，则意味着该待搜索值不存在并返回 -1
    return DOES_NOT_EXIST;
}

console.log(binarySearch([5, 4, 3, 2, 1], 3))
// ---------------------------

function interpolationSearch(
    array,
    value,
    compareFn = defaultCompare,
    equalsFn = defaultEquals,
    diffFn = defaultDiff
) {

    // 没有排序的话，对于未排序的数组就找不到对应索引了
    array = quickSort(array);

    const { length } = array;
    let low = 0;
    let high = length - 1;
    let position = -1;
    let delta = -1;
    while (
        low <= high
        && biggerEquals(value, array[low], compareFn)
        && lesserEquals(value, array[high], compareFn)
    ) {
        delta = diffFn(value, array[low]) / diffFn(array[high], array[low]);
        position = low + Math.floor((high - low) * delta);
        if (equalsFn(array[position], value)) {
            return position;
        }
        if (compareFn(array[position], value) === Compare.LESS_THAN) {
            low = position + 1;
        } else {
            high = position - 1;
        }
    }
    return DOES_NOT_EXIST;
}

console.log(interpolationSearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4))

console.log(interpolationSearch([5, 4, 3, 2, 1], 3))

// ==============
function shuffle(array) {
    let currentIndex = array.length;
    while (currentIndex !== 0) {
        const randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;
        swap(array, currentIndex, randomIndex);
    }
    return array;
}
// 每次输出结果可能不一样
console.log(shuffle([5, 4, 3, 2, 1])) // [ 3, 2, 5, 1, 4 ]
