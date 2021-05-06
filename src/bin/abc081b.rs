use proconio::input;

fn main() {
    input! {
        n: usize,
        a: [usize; n],
    };

    let each_divible: Vec<usize> = a.iter().map(|n| count_divible(n)).collect();
    println!("{}", each_divible.iter().min().unwrap());
}

fn count_divible(n: &usize) -> usize {
    let mut n = *n;
    let mut cnt = 0;
    while n % 2 == 0 {
        cnt += 1;
        n /= 2;
    }
    cnt
}
