use std::fs;
use std::collections::HashMap;
use std::collections::HashSet;


fn find_all_paths(graph: HashMap<&i32, Vec<i32>>, start: i32, end: i32, mut path: Vec<i32>) -> Vec<Vec<i32>> {
    path.push(start);
    println!("{:?}", path);
    if start == end {
        let x = Vec::new();
        return path;
    }
    if !graph.contains_key(&start) {
        return Vec::new();
    }
    let mut paths: Vec<Vec<i32>> = Vec::new();
    for node in &graph[&start] {
        if !path.contains(&node) {
            let newpaths = find_all_paths(graph.clone(), *node, end, path.clone());
            for newpath in newpaths {
                paths.push(newpath);
            }
        }
    }
    return paths
}


fn main() {
    let contents = fs::read_to_string("input.txt").expect(
        "Something went wrong reading the file",
    );
    let mut adapters: Vec<i32> = contents
        .lines()
        .map(|x| { x.parse::<i32>().unwrap() })
        .collect();
    adapters.sort();
    let last = adapters.last().unwrap() + 3;
    adapters.push(last);
    adapters.insert(0, 0);
    let vals = adapters.iter();
    let next_vals = adapters.iter().skip(1);

    let result: Vec<i32> = vals.zip(next_vals).map(|(cur, next)| next - cur).collect();
    let one_jolt = result.iter().filter(|&x| { *x == 1 }).count();
    let three_jolt = result.iter().filter(|&x| { *x == 3 }).count();
    println!("Part 1: {}", one_jolt * three_jolt);
    let mut graph = HashMap::new();
    for adapter in &adapters {
        let mut neighbors = Vec::new();
        for i in 1..4 {
            if adapters.contains(&(adapter + i)) {
                neighbors.push(adapter + i);
            }
        }
        graph.insert(adapter, neighbors);
    }
    println!("{:?}", graph);
    let paths = find_all_paths(graph, 0, 140, Vec::new());
}
