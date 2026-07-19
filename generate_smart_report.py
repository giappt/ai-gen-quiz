import subprocess
import csv
import io
import os

def get_git_file_content(commit, filepath):
    try:
        content = subprocess.check_output(['git', 'show', f'{commit}:{filepath}'], text=True)
        return content
    except subprocess.CalledProcessError:
        return None

def generate_smart_report():
    try:
        status_output = subprocess.check_output(['git', 'diff', 'HEAD~1', '--name-status'], text=True)
    except subprocess.CalledProcessError:
        print("Lỗi khi chạy git diff.")
        return

    files_changed = []
    for line in status_output.strip().split('\n'):
        if line.startswith('M') or line.startswith('A'):
            parts = line.split('\t')
            if len(parts) >= 2 and parts[1].endswith('.csv'):
                files_changed.append(parts[1])

    report = ["# Báo Cáo Chi Tiết Nội Dung Đã Sửa (Từng File)\n"]
    report.append("Báo cáo này đối chiếu chính xác từng ô (column) bị thay đổi giữa bản cũ và bản mới, kèm theo lý do.\n")

    total_files = len(files_changed)
    print(f"Đang xử lý {total_files} files...")

    for filepath in sorted(files_changed):
        old_content = get_git_file_content('HEAD~1', filepath)
        if not old_content:
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            new_content = f.read()

        old_reader = list(csv.reader(io.StringIO(old_content)))
        new_reader = list(csv.reader(io.StringIO(new_content)))

        file_report = []
        
        # Compare row by row
        min_rows = min(len(old_reader), len(new_reader))
        for r in range(min_rows):
            old_row = old_reader[r]
            new_row = new_reader[r]
            
            # Pad rows if different lengths
            max_cols = max(len(old_row), len(new_row))
            old_row += [''] * (max_cols - len(old_row))
            new_row += [''] * (max_cols - len(new_row))

            for c in range(max_cols):
                if old_row[c] != new_row[c]:
                    old_val = old_row[c]
                    new_val = new_row[c]
                    
                    reason = []
                    if ' của ' in old_val and ' của ' not in new_val:
                        reason.append("Sửa lỗi dịch thuật (xóa chữ 'của' thừa)")
                    if ("'" in old_val or '"' in old_val) and ('「' in new_val or '」' in new_val):
                        reason.append("Chuẩn hóa dấu ngoặc kép thành 「」")
                    if old_val == '' and new_val != '':
                        reason.append("Khôi phục dữ liệu bị khuyết (ghép từ các chunk)")
                        
                    if not reason:
                        reason.append("Chỉnh sửa format/dấu câu/nội dung khác")
                        
                    reason_str = " + ".join(reason)
                    
                    # Rút gọn text nếu quá dài
                    show_old = old_val if len(old_val) < 100 else old_val[:50] + "..." + old_val[-50:]
                    show_new = new_val if len(new_val) < 100 else new_val[:50] + "..." + new_val[-50:]
                    if old_val == '': show_old = "[Trống]"
                    
                    file_report.append(f"- **Dòng {r+1}, Cột {c+1}**: {reason_str}")
                    file_report.append(f"  - Cũ: `{show_old}`")
                    file_report.append(f"  - Mới: `{show_new}`")

        if file_report:
            report.append(f"\n### File: `{filepath}`")
            report.extend(file_report)

    # Ghi ra file
    os.makedirs('review', exist_ok=True)
    with open('review/detailed_changes.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))
        
    print("Hoàn tất tạo file review/detailed_changes.md")

if __name__ == "__main__":
    generate_smart_report()
