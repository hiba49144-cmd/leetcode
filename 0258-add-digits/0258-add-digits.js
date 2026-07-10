/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
    while (num >= 10) {
        let total = 0;

        while (num > 0) {
            total += num % 10;
            num = Math.floor(num / 10);
        }

        num = total;
    }

    return num;
}
console.log(addDigits(38))
console.log(addDigits(0))