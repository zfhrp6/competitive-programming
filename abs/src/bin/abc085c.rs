use proconio::input;

fn main() {
    input! {
        n: usize,
        y: usize,
    }

    for x in (0..=n).rev() {
        if n < x{
            continue;
        }
        for v in (0..=(n - x)).rev() {
            if n < x + v {
                continue;
            }
            let i = n - x - v;
            if (x * 10 + v * 5 + i * 1) * 1000 == y {
                println!("{} {} {}", x, v, i);
                std::process::exit(0);
            }
        }
    }

    println!("-1 -1 -1");
}
