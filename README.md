<a href="https://github.com/Matatika/analyze-meltano/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/Matatika/analyze-meltano"></a>
# analyze-meltano

Meltano project [file bundle](https://meltano.com/docs/command-line-interface.html#file-bundle) of Matatika datasets for `tap-meltano`. These datasets are automatically added to your Matatika workspace when you initialize a 
`tap-meltano` pipeline.

Files:
- [`analyze/datasets`](./bundle/analyze/datasets) (directory)

### Adding this file bundle to your own Meltano project

Add plugin to `discovery.yml`:
```yaml
files:
- name: analyze-meltano
  namespace: tap_meltano
  repo: https://github.com/Matatika/analyze-meltano
  pip_url: git+https://github.com/Matatika/analyze-meltano.git
```

Add plugin to your Meltano project:
```bash
# Add only the file bundle
meltano add files analyze-meltano

# Add the file bundle as a related plugin through adding the Meltano extractor
meltano add extractor --include-related tap-meltano
```
