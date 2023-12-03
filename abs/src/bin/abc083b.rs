use proconio::input;

fn main() {
    input! {
        n: usize,
        a: usize,
        b:usize,
    }

    let mut ans = 0;
    for i in 1..=n {
        let digit_sum = sum_digit(i);
        ans += if (a <= digit_sum) && (digit_sum <= b) {
            i
        } else {
            0
        }
    }
    println!("{}", ans);
}

fn sum_digit(n: usize) -> usize {
    let n_string = n.to_string();
    let mut sum = 0;
    for c in n_string.chars() {
        sum += c.to_digit(10).unwrap();
    }
    sum as usize
}
