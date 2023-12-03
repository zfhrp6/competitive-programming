use std::io::{stdin, stdout, Write};

fn main() {
    for _ in 0..1000 {
        let mut line: String = String::new();
        stdin().read_line(&mut line).unwrap();
        let mut splits = line.split_whitespace();
        let sx:usize = splits.next().unwrap().parse().unwrap();
        let sy:usize = splits.next().unwrap().parse().unwrap();
        let tx:usize = splits.next().unwrap().parse().unwrap();
        let ty:usize = splits.next().unwrap().parse().unwrap();

        for _ in 0..abs(&sx, &tx) {
            let c = if &sx > &tx { "U" } else { "D" };
            print!("{}", c);
        }
        for _ in 0..abs(&sy, &ty) {
            let c = if &sy > &ty { "L" } else { "R" };
            print!("{}", c);
        }
        println!("");
        stdout().flush().unwrap();
        stdin().read_line(&mut line).unwrap();
    }
}

fn abs(a: &usize, b: &usize) -> usize {
    if a > b {
        a - b
    } else {
        b - a
    }
}