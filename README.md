# Excel Modifier
Excel modifier is a Python package for editing Excel files. It provides a convenient interface to modify comments in Excel files, allowing users to update comments for specific cells.

```markdown
## Installation

You can install Excel modifier using pip:

```bash
pip install excel_modifier
```

## Usage

### Quick Start

1. Import the `ExcelMode` class from the `excel_modifier` package.
2. Initialize `ExcelMode` with the path to your Excel file.
3. Use the `set_comment` method to update the comment for a specific cell.
4. Save the changes using the `save` method.

```python
from excel_modifier import ExcelMode

# Initialize ExcelMode with the path to your Excel file
excel_mode = ExcelMode('path/to/your/excel/file.xlsx')

# Set a comment in a specific cell
excel_mode.set_comment('A1', 'This is a comment')

# Save the changes to the Excel file
excel_mode.save()
```


## Features

- **Edit Excel Comments**: Update comments for specific cells in Excel files.

## Contributing

Contributions are welcome! If you encounter any issues or have feature requests, please submit them through GitHub issues. Pull requests are also appreciated.

Before contributing, please read the [Contributing Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This README provides clear and concise instructions on how to install the package, a quick start guide for basic usage, information on advanced usage, a feature list, guidelines for contributing, and license information. It aims to be user-friendly and informative for potential users and contributors.