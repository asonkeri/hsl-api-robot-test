# HSL Routing Api Robot Tests

Robot Framework tests and a small helper library for HSL Routing GraphQL API.

## Usage

- Install dependencies: `pip install -r requirements.txt`
- Set `HSL_API_KEY` environment variable e.g. `export HSL_API_KEY=xxxxxxxxxx`
- Run robot tests: `robot -d results hsl.robot`
- Run helper library unit tests: `pytest`
