use proconio::input;

fn main() {
    input! {
        n: usize,
        mut a: [usize; n],
    }

    a.sort();
    a.reverse();
    let mut score_a = 0;
    let mut score_b = 0;
    for (idx, card) in a.iter().enumerate() {
        if idx % 2 == 0 {
            score_a += card;
        } else {
            score_b += card;
        }
    }

    println!("{}", score_a - score_b);
}
