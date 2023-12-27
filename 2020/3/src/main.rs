use std::fs;


fn traverse(map: Vec<Vec<char>>, right: i32, down: i32) -> i32 {
    let mut y = 0i32;
    let mut x = 0i32;
    let mut trees = 0i32;
    let width = map[0].len() as i32;
    while y < map.len() as i32 {
        trees += match map[y as usize][x as usize] {
            '.' => 0,
            '#' => 1,
            _ => 0,
        };
        x = (x + right) % width;
        y += down;
    }
    trees
}


fn main() {
    let contents = fs::read_to_string("input.txt").expect(
        "Something went wrong reading the file",
    );
    let map: Vec<Vec<char>> = contents.lines().map(|x| {
        x.chars().collect()
    }).collect();
    println!("Part 1: {}", traverse(map.clone(), 3, 1));
    let slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ];
    let mut result = 1i64;
    for (right, down) in slopes.iter() {
        result *= traverse(map.clone(), *right, *down) as i64;
    }
    println!("Part 2: {}", result);
}
