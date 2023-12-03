use proconio::input;

fn main() {
    input! {
        n: usize,
        mut d: [usize; n],
    }

    d.sort();

    let mut last_mochi_size = 0;
    let mut cnt = 0;
    for mochi in d {
        if mochi <= last_mochi_size {
            continue;
        }

        cnt += 1;
        last_mochi_size = mochi;
    }

    println!("{}", cnt);
}
