use proconio;

struct MoveAction {
    before_row: usize,
    before_col: usize,
    after_row: usize,
    after_col: usize,
}

struct ConnectAction {
    c1_row: usize,
    c1_col: usize,
    c2_row: usize,
    c2_col: usize,
}

struct Result {
    moves: Vec<MoveAction>,
    connects: Vec<ConnectAction>,
}

impl Result {
    fn new(moves: Vec<MoveAction>, connects: Vec<ConnectAction>) -> Result {
        Result {
            moves: moves,
            connects: connects,
        }
    }
}

fn calc_score(n: usize, field: Vec<String>, result: &Result) -> usize {
    unimplemented!();
}

fn print_answer(result: &Result) {
    println!("{}", result.moves.len());
    for move_action in &result.moves {
        println!(
            "{} {} {} {}",
            move_action.before_row,
            move_action.before_col,
            move_action.after_row,
            move_action.after_col,
        );
    }
    println!("{}", result.connects.len());
    for connect_action in &result.connects {
        println!(
            "{} {} {} {}",
            connect_action.c1_row,
            connect_action.c1_col,
            connect_action.c2_row,
            connect_action.c2_col
        );
    }
}

fn split(s: &str) -> Vec<usize> {
    s.chars().map(|x| ((x as i32) - ('0' as i32)) as usize).collect()
}

fn main() {
    proconio::input! {
        n: usize,
        k: usize,
        cc: [String; n],
    }

    println!("{}", n);
    println!("{}", k);
    let c = cc.iter().map(|c| split(c));
    for row in c {
        let mut idx = 0;
        for cell in &row {
            if idx > 0 {
                print!(" ");
            }
            print!("{}", cell);
            if idx == (&row.len() - 1) {
                println!("");
            }
            idx+=1;
        }
    }

    print_answer(&Result{
        moves: vec![],
        connects: vec![],
    })
}
