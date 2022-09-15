import pytest
import string
import numpy as np

from vectorlab.stats import DegreeGraph

n_samples = 100
urls = np.array(
    [
        f'www.test.com/samples/{i}'
        for i in range(n_samples)
    ]
)


@pytest.mark.parametrize('split_token', ['/'])
@pytest.mark.parametrize('wild_token', ['*'])
@pytest.mark.parametrize('threshold', [n_samples, n_samples + 1])
@pytest.mark.parametrize('failed_safe', ['invalid'])
def test_deg_graph(split_token, wild_token, threshold, failed_safe):

    deg_graph = DegreeGraph(
        split_token=split_token,
        wild_token=wild_token,
        deg_threshold=threshold,
        failed_safe=failed_safe
    )

    transformed_urls = deg_graph.fit_transform(urls)

    if threshold <= n_samples:
        transformed_urls_ = np.array(
            [f'www.test.com/samples/{wild_token}'] * n_samples
        )
        assert (transformed_urls == transformed_urls_).all()
    else:
        assert (transformed_urls == urls).all()

    # Some random input
    random_urls = [
        ''.join(np.random.choice(list(string.ascii_lowercase), 20))
        for i in range(n_samples)
    ]

    invalid_transformed_urls = deg_graph.transform(random_urls)
    failed_safe_urls = np.array([failed_safe] * n_samples)

    assert (invalid_transformed_urls == failed_safe_urls).all()
