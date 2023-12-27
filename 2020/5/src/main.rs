use std::fs;


fn main() {
    let contents = fs::read_to_string("input.txt").expect(
        "Something went wrong reading the file",
    );
    let mut pass_ids = Vec::new();
    for pass in contents.lines() {
        let mut rows: Vec<i32> = (0..128).collect();
        let mut cols: Vec<i32> = (0..8).collect();
        for c in pass.chars() {
            match c {
                'F' => rows = rows[0..rows.len()/2].to_vec(),
                'B' => rows = rows[rows.len()/2..].to_vec(),
                'L' => cols = cols[0..cols.len()/2].to_vec(),
                'R' => cols = cols[cols.len()/2..].to_vec(),
                _ => {},
            }
        }
        let row = rows[0];
        let col = cols[0];
        pass_ids.push((row * 8) + col);
    }
    println!("Part 1: {:?}", pass_ids.iter().max());
    for r in 1..127 {
        for c in 0..8 {
            let id: i32 = (r * 8) + c;
            let low = id - 1;
            let high = id + 1;
            if !pass_ids.contains(&id) && pass_ids.contains(&low) && pass_ids.contains(&high) {
                println!("Part 2: {}", id);
                break;
            }
        }
    }
}
