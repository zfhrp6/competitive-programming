use petgraph::algo::dijkstra;
use petgraph::graph::{NodeIndex, UnGraph};
use rand::{thread_rng, Rng};
use std::cmp::Ordering;
use std::collections::HashMap;
use std::io::{stdin, stdout, Write};

struct Point {
    x: usize,
    y: usize,
}

fn usize(p1: &Point, p2: &Point) -> usize {
    let p1 = if p1 < p2 { p1 } else { p2 };
    let p2 = if p1 >= p2 { p1 } else { p2 };
    (p1.x * 100 + p1.y) * 10000 + (p2.x * 100 + p2.y)
}

impl From<&Point> for NodeIndex<usize> {
    fn from(p: &Point) -> NodeIndex<usize> {
        NodeIndex::from(&p.x * 100 + &p.y)
    }
}

impl PartialEq for Point {
    fn eq(&self, other: &Self) -> bool {
        self.x == other.x && self.y == other.y
    }
}

impl Eq for Point {}

impl PartialOrd for Point {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        if self.x != other.x {
            Some(self.x.cmp(&other.x))
        } else {
            Some(self.y.cmp(&other.y))
        }
    }
}

impl Ord for Point {
    fn cmp(&self, other: &Self) -> Ordering {
        if self.x != other.x {
            self.x.cmp(&other.x)
        } else {
            self.y.cmp(&other.y)
        }
    }
}

fn main() {
    let mut graph = init_graph();
    let mut edges: HashMap<usize, (usize, String)> = HashMap::new();
    for _ in 0..1000 {
        let (s, t) = read_query();
        let distance = distance(&s, &t);

        let min_st = if s < t { &s } else { &t };
        let max_st = if s >= t { &s } else { &t };

        let memo_route = edges.get(&usize(&s, &t));
        let route: String;
        if memo_route.is_some() && memo_route.unwrap().0 < ((distance as f32) * 0.5) as usize {
            route = memo_route.unwrap().1.to_string();
        } else {
            route = random_route(&s, &t).to_owned();
        }
        println!("{}", route);
        stdout().flush().unwrap();
        let _result = read_result();
        edges.insert(usize(&s, &t), (_result, route));
        // update_edge(&mut graph, &s, &t, _result);
    }
}

fn distance(s: &Point, t: &Point) -> usize {
    (if s.x > t.x { s.x - t.x } else { t.x - s.x })
        + (if s.y > t.y { s.y - t.y } else { t.y - s.y })
}

fn random_route(s: &Point, t: &Point) -> String {
    let mut route: String = "".to_string();
    let x_dif_sig = s.x > t.x;
    let x_move = if x_dif_sig { "U" } else { "D" };
    let mut x_dif = abs(&s.x, &t.x);

    let y_dif_sig = s.y > t.y;
    let y_move = if y_dif_sig { "L" } else { "R" };
    let mut y_dif = abs(&s.y, &t.y);

    let mut rng = thread_rng();

    let move_cnt = y_dif + x_dif;

    for _ in 0..move_cnt {
        if y_dif == 0 {
            route.push_str(x_move);
            x_dif -= 1;
            continue;
        }
        if x_dif == 0 {
            route.push_str(y_move);
            y_dif -= 1;
            continue;
        }
        if rng.gen_bool(0.5) {
            route.push_str(x_move);
            x_dif -= 1;
            continue;
        } else {
            route.push_str(y_move);
            y_dif -= 1;
            continue;
        }
    }
    route
}

fn update_edge(g: &mut UnGraph<(usize, usize), f32, usize>, s: &Point, t: &Point, weight: f32) {
    if g.find_edge_undirected(s.into(), t.into()).is_some() {
        g.update_edge(s.into(), t.into(), weight);
    } else {
        g.add_edge(s.into(), t.into(), weight);
    }
}

fn abs(a: &usize, b: &usize) -> usize {
    if a > b {
        a - b
    } else {
        b - a
    }
}

fn read_query() -> (Point, Point) {
    let mut line: String = String::new();
    stdin().read_line(&mut line).unwrap();
    let mut splits = line.split_whitespace();
    let sx: usize = splits.next().unwrap().parse().unwrap();
    let sy: usize = splits.next().unwrap().parse().unwrap();
    let tx: usize = splits.next().unwrap().parse().unwrap();
    let ty: usize = splits.next().unwrap().parse().unwrap();
    (Point { x: sx, y: sy }, Point { x: tx, y: ty })
}

fn read_result() -> usize {
    let mut line: String = String::new();
    stdin().read_line(&mut line).unwrap();
    let mut splits = line.split_whitespace();
    splits.next().unwrap().parse().unwrap()
}

fn init_graph() -> UnGraph<(usize, usize), f32, usize> {
    let mut edges: Vec<(usize, usize, f32)> = vec![];
    for x in 0..29 {
        for y in 0..29 {
            edges.push((100 * x + y, 100 * x + y + 1, 0.5));
            edges.push((100 * x + y, 100 * (x + 1) + y, 0.5));
        }
        edges.push((100 * x + 29, 100 * (x + 1) + 29, 0.5));
        edges.push((100 * 29 + x, 100 * 29 + 100 * x + 1, 0.5));
    }
    UnGraph::<(usize, usize), f32, usize>::from_edges(&edges)
}
