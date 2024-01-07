const std = @import("std");
const Allocator = std.mem.Allocator;
const GeneralPurposeAllocator = std.heap.GeneralPurposeAllocator;

pub fn calc_floor(content: []const u8) isize {
    var floor: isize = 0;
    for (content) |char| {
        if (char == '(') {
            floor += 1;
        } else if (char == ')') {
            floor -= 1;
        }
    }
    return floor;
}

pub fn calc_basement_entering_pos(content: []const u8) ?usize {
    var floor: isize = 0;
    var pos: ?usize = null;
    for (content, 0..) |char, index| {
        if (char == '(') {
            floor += 1;
        } else if (char == ')') {
            floor -= 1;
        }
        if (floor == -1) {
            pos = index + 1; // Position start at index 1
            break;
        }
    }
    return pos;
}

pub fn readFileContents(allocator: *std.mem.Allocator, inputPath: []const u8) ![]u8 {
    // Open the file for reading
    const file = try std.fs.cwd().openFile(inputPath, .{ .mode = .read_only });
    defer file.close();

    // Determine the size of the file
    const fileSize = try file.getEndPos();

    // Allocate a buffer to hold the file contents
    var buffer = try allocator.alloc(u8, fileSize);

    // Read the file into the buffer
    _ = try file.readAll(buffer);

    // Return a slice of the buffer containing the read data
    return buffer[0..fileSize];
}

pub fn main() !void {
    const filepath = "input.txt";

    var gpa = GeneralPurposeAllocator(.{}){}; // Instantiate the allocator
    var allocator = gpa.allocator(); // Obtain the allocator interface as a mutable variable
    defer {
        const deinitStatus = gpa.deinit();
        if (deinitStatus == .leak) {
            std.debug.print("Memory leak detected\n", .{});
        }
    }
    const content_buffer = try readFileContents(&allocator, filepath);
    defer allocator.free(content_buffer);

    const floor = calc_floor(content_buffer);
    std.debug.print("The floor Santa needs to reach is: {}\n", .{floor});

    const basement_pos: ?usize = calc_basement_entering_pos(content_buffer);
    std.debug.print("The position of the character to enter the basement is: {?}\n", .{basement_pos});
}

test "first challenge" {
    const testContent = "))(((((";
    const floor = calc_floor(testContent);
    std.debug.print("The floor Santa needs to reach is: {}\n", .{floor});
}

test "second challenge" {
    const testContent = "()())";
    const basement_pos: ?usize = calc_basement_entering_pos(testContent);
    std.debug.print("The position of the character to enter the basement is: {?}\n", .{basement_pos});
}
