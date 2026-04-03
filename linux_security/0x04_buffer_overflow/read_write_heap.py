cat > read_write_heap.py << 'EOF'
#!/usr/bin/env python3
import sys

def error_function():
    '''Print usage and exit with status 1'''
    print("Usage: read_write_heap.py pid search_string replace_string", file=sys.stderr)
    sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        error_function()

    try:
        pid = int(sys.argv[1])
    except ValueError:
        print("Error: PID must be a number", file=sys.stderr)
        sys.exit(1)

    search_string = sys.argv[2]
    replace_string = sys.argv[3]

    if len(search_string) == 0 or len(replace_string) == 0:
        error_function()

    if len(replace_string) > len(search_string):
        print("Error: replace_string cannot be longer than search_string", file=sys.stderr)
        sys.exit(1)

    search = search_string.encode('ascii')
    replace = replace_string.encode('ascii')

    maps_path = f"/proc/{pid}/maps"
    mem_path = f"/proc/{pid}/mem"

    try:
        # Find heap
        heap_start = 0
        heap_end = 0

        with open(maps_path, 'r') as maps:
            for line in maps:
                if '[heap]' in line:
                    addr = line.split()[0]
                    heap_start = int(addr.split('-')[0], 16)
                    heap_end = int(addr.split('-')[1], 16)
                    break

        if heap_start == 0:
            print(f"Error: Heap not found for PID {pid}", file=sys.stderr)
            sys.exit(1)

        # Open memory and replace
        with open(mem_path, 'rb+') as mem:
            mem.seek(heap_start)
            heap_content = mem.read(heap_end - heap_start)

            offset = heap_content.find(search)
            if offset == -1:
                print(f"String '{search_string}' not found in heap", file=sys.stderr)
                sys.exit(0)

            # Write replacement
            mem.seek(heap_start + offset)
            mem.write(replace)

            # Pad with null bytes if replace is shorter
            if len(replace) < len(search):
                mem.write(b'\x00' * (len(search) - len(replace)))

            print(f"Success: Replaced '{search_string}' with '{replace_string}' at offset {hex(offset)}")

    except PermissionError:
        print("Error: Permission denied. Run the script with sudo.", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: Process with PID {pid} not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
EOF
