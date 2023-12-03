use whiteread::parse_line;

fn main() {
    let (a, b): (i32, i32) = parse_line().unwrap();

    println!("{}", if a * b % 2 == 1 { "Odd" } else { "Even" });
}
