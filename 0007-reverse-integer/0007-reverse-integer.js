/**
 * @param {number} x
 * @return {number}
 */
const reverse = function(x) {
    let sign = Math.sign(x);

    let rev = parseInt(Math.abs(x).toString().split("").reverse().join("")) * sign;

    if (rev < -(2 ** 31) || rev > (2 ** 31 - 1)) {
        return 0;
    }

    return rev;
}
console.log(reverse(123))
console.log(reverse(-123))
console.log(reverse(120))