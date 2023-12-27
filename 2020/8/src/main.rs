use std::fs;

fn parse(code: &[(&str, i32)]) -> (i32, Vec<i32>, bool) {
    let mut acc = 0;
    let mut i = 0i32;
    let mut visited = Vec::new();
    let mut inf = false;
    while i < code.len() as i32 {
        if visited.contains(&i) {
            inf = true;
            break;
        }
        visited.push(i);
        match code[i as usize] {
            ("jmp", value) => {
                i += value;
            }
            ("acc", value) => {
                acc += value;
                i +=1;
            }
            ("nop", _) =>{
                i += 1;
            }
            _ => break,
        }
    }
    return (acc, visited, inf);
}

fn main() {
    let contents = fs::read_to_string("input.txt").expect(
        "Something went wrong reading the file",
    );
    let mut code: Vec<(&str, i32)> = contents.lines().map(|row| {
        let x: Vec<&str> = row.split(' ').collect();
        (x[0], x[1].parse::<i32>().unwrap())
    }).collect();

    let (part_1, visited, _) = parse(&code);
    println!("Part 1: {}", part_1);

    for i in visited {
        let line = code[i as usize];
        if line.0 == "acc" {
            continue;
        }

        code[i as usize] = match line {
            ("jmp", value) => ("nop", value),
            ("nop", value) => ("jmp", value),
            _ => line,
        };
        let (part_2, _, inf) = parse(&code);
        if !inf {
            println!("Part 2: {}", part_2);
            println!("Row: {} {:?}", i + 1, line);
            break;
        }
        code[i as usize] = line;
    }
}
