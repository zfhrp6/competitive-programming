use proconio::input;

fn main() {
    input! {
        a: usize,
        b: usize,
        c: usize,
        x: usize,
    }

    let mut ans = 0;
    for h5 in 0..=a {
        for h1 in 0..=b {
            for c5 in 0..=c {
                if h5 * 500 + h1 * 100 + c5 * 50 == x {
                    ans += 1;
                }
            }
        }
    }
    println!("{}", ans);
}
