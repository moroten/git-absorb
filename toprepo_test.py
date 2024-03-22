#!/user/bin/env python3
import pytest

import toprepo


def test_usage_help():
    with pytest.raises(SystemExit) as pytest_err:
        toprepo.main(["argv0"])
    assert pytest_err.type == SystemExit
    assert pytest_err.value.code == 2


def test_push_refspec_parser():
    assert toprepo.PushRefSpec.parse("abc:refs/def") == toprepo.PushRefSpec(
        local_ref="abc", remote_ref="refs/def"
    )
    assert toprepo.PushRefSpec.parse("main") == toprepo.PushRefSpec(
        local_ref="refs/heads/main", remote_ref="refs/heads/main"
    )
    assert toprepo.PushRefSpec.parse("pr/foo") == toprepo.PushRefSpec(
        local_ref="refs/heads/pr/foo", remote_ref="refs/heads/pr/foo"
    )
    with pytest.raises(ValueError, match="Multiple ':' "):
        toprepo.PushRefSpec.parse("a:b:c")


def repository_basename():
    assert toprepo.repository_basename("https://github.com/org/repo") == "repo"
    assert toprepo.repository_basename("https://github.com/org/repo.git") == "repo"
    assert toprepo.repository_basename("git://github.com:repo") == "repo"
    assert toprepo.repository_basename("abc\\org\\repo") == "repo"
