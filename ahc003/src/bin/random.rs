use std::io::{stdin, stdout, Write};
use rand::{thread_rng, Rng};
use num_bigint::BigUint;
use num_traits::{Zero};
use num_bigint::ToBigUint;

fn main() {
    let mut whole_move_distance: BigUint = Zero::zero();
    let mut whole_move_count: BigUint = Zero::zero();
    for _ in 0..1000 {
        let mut line: String = String::new();
        stdin().read_line(&mut line).unwrap();
        let mut splits = line.split_whitespace();
        let sx:usize = splits.next().unwrap().parse().unwrap();
        let sy:usize = splits.next().unwrap().parse().unwrap();
        let tx:usize = splits.next().unwrap().parse().unwrap();
        let ty:usize = splits.next().unwrap().parse().unwrap();
        eprintln!("({}, {}) -> ({}, {})", sx, sy, tx, ty);

        let x_dif_sig = &sx > &tx;
        let x_move = if x_dif_sig {"U"} else {"D"};
        let mut x_dif = abs(&sx, &tx);
        
        let y_dif_sig = &sy > &ty;
        let y_move = if y_dif_sig {"L"} else {"R"};
        let mut y_dif = abs(&sy, &ty);

        let mut rng = thread_rng();

        let move_cnt = y_dif + x_dif;
        whole_move_count += &move_cnt.to_biguint().unwrap();

        for _ in 0..move_cnt {
            if y_dif == 0 {
                print!("{}", x_move);
                x_dif -= 1;
                continue;
            }
            if x_dif == 0 {
                print!("{}", y_move);
                y_dif -= 1;
                continue;
            }
            if rng.gen_bool(0.5) {
                print!("{}", x_move);
                x_dif -= 1;
                continue;
            }
            else {
                print!("{}", y_move);
                y_dif -= 1;
                continue;
            }
        }
        println!("");
        stdout().flush().unwrap();
        stdin().read_line(&mut line).unwrap();
        splits = line.split_whitespace();
        let result: usize = splits.next().unwrap().parse().unwrap();
        eprintln!("{}", result);
        whole_move_distance += result.to_biguint().unwrap();
    }
    eprintln!("whole move count: {}\nwhole distance: {}", whole_move_count, whole_move_distance);
}

fn abs(a: &usize, b: &usize) -> usize {
    if a > b {
        a - b
    } else {
        b - a
    }
}
