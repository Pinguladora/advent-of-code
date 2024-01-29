-- Function to split a string by a delimiter
local function split_string(input)
    local res = {}
    for match in input:gmatch("%S+") do
        table.insert(res, match)
    end
    return res
end

-- Read and split file contents
local function read_file_into_table(path)
    local file = io.open(path, "r")
    local instructions = {}
    if not file then
        return nil, "Error opening file."
    end

    for line in file:lines() do
        line = line:gsub(",", "")
        line = split_string(line)
        table.insert(instructions, line)
    end
    file:close()
    return instructions
end

local function apply_instruction(instruction, register_val, position, offset)
    if instruction == "hlf" then
        register_val = register_val // 2
        position = position + 1
    elseif instruction == "tpl" then
        register_val = register_val * 3
        position = position + 1
    elseif instruction == "inc" then
        register_val = register_val + 1
        position = position + 1
    elseif instruction == "jie" then
        position = (register_val % 2 == 0) and (position + offset) or (position + 1)
    elseif instruction == "jio" then
        position = (register_val == 1) and (position + offset) or (position + 1)
    end
    return register_val, position
end

local function exec_instructions(instructions, registers)
    local i = 1
    while i>0 and i <= #instructions do
        local instruction, action, offset = table.unpack(instructions[i])
        offset = tonumber(offset) or 0
        if instruction == "jmp" then
            i = i + action
        else
            registers[action], i = apply_instruction(instruction, registers[action], i, offset)
        end
    end
    return registers
end

local function main(path)
    local instructions, err = read_file_into_table(path)
    if instructions then
        local registers = exec_instructions(instructions, { a = 0, b = 0 })
        print("First challenge: the value for register b is " .. registers["b"])

        registers = exec_instructions(instructions, { a = 1, b = 0 })
        print("Second challenge: the value for register b is " .. registers["b"])
    else
        error(string.format("Error reading file %s: %s", path, err))
    end
end

local path = "input.txt"
main(path)
