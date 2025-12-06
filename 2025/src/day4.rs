use anyhow::{bail, Result};

fn neighbors(row: isize, col: isize) -> [(isize, isize); 8] {
    [
        (row - 1, col - 1),
        (row - 1, col),
        (row - 1, col + 1),
        (row, col - 1),
        (row, col + 1),
        (row + 1, col - 1),
        (row + 1, col),
        (row + 1, col + 1),
    ]
}

fn part1(lines: Vec<&str>) -> Result<()> {
    let mut papers = Vec::new();

    for line in lines {
        papers.push(line.chars().into_iter().map(|c| (c == '@') as u8).collect::<Vec<u8>>());
    }

    let mut roll_count = 0;

    for row_idx in 0..papers.len() as isize {
        for col_idx in 0..papers[row_idx as usize].len() as isize {
            let neighbors = neighbors(row_idx, col_idx);

            if papers[row_idx as usize][col_idx as usize] == 0 {
                continue;
            }

            let neighboring_rolls = neighbors.iter().map(|(r,c)| {
                if *r < 0 || *c < 0 {
                    return &0;
                }
                papers.get(*r as usize).and_then(|row| row.get(*c as usize)).unwrap_or(&0)
            }).sum::<u8>();

            if neighboring_rolls < 4 {
                roll_count += 1;
            }
        }
    }

    println!("Part 1: {}", roll_count);

    Ok(())
}

fn part2(lines: Vec<&str>) -> Result<()> {
    let mut papers = Vec::new();

    for line in lines {
        papers.push(line.chars().into_iter().map(|c| (c == '@') as u8).collect::<Vec<u8>>());
    }

    let mut roll_count = 0;

    let mut old_papers = vec![vec![0u8]];

    while old_papers != papers {
        old_papers = papers.clone();

        for row_idx in 0..papers.len() as isize {
            for col_idx in 0..papers[row_idx as usize].len() as isize {
                let neighbors = neighbors(row_idx, col_idx);

                if papers[row_idx as usize][col_idx as usize] == 0 {
                    continue;
                }

                let neighboring_rolls = neighbors.iter().map(|(r,c)| {
                    if *r < 0 || *c < 0 {
                        return &0;
                    }
                    papers.get(*r as usize).and_then(|row| row.get(*c as usize)).unwrap_or(&0)
                }).sum::<u8>();

                if neighboring_rolls < 4 {
                    roll_count += 1;
                    papers[row_idx as usize][col_idx as usize] = 0;
                }
            }
        }
    }


    println!("Part 2: {}", roll_count);

    Ok(())
}

pub fn run(file_data: String) -> Result<()> {
    let test_data = r#"..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."#.to_string();

    let lines = file_data
        .split(|b| b == '\n')
        .map(|line| line.strip_suffix(&['\r']).unwrap_or(line)).collect::<Vec<&str>>();

    part2(lines)?;

    Ok(())
}