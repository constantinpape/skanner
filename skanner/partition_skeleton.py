import numpy as np
import nifty
import nifty.graph.rag as nrag
# TODO implement the same for distro graph


def partition_object_from_skeleton(skeleton, rag, node_labeling,
                                   edge_weights, object_id, skel_paths):
    # find the fragments that were labeled with the object ids
    fragment_ids = np.where(node_labeling == object_id)[0]

    # find edges within, to and outside of the object
    uv_ids = rag.uvIds()
    edge_states = (uv_ids == object_id).reshape(uv_ids.shape)
    edge_states = np.sum(edge_states, axis=1)
    # edges in the object
    in_edges = edge_states == 2
    # edges to and outside of the object
    out_edges = edge_states == 0

    # set the weights for graph watershed
    weights = edge_weights.copy()
    # set all outside edges to be maximally repulsive
    weights[out_edges] = 5 * edge_weights.max()

    # compute the seeds from skeleton paths
    node_seeds = np.zeros_like(node_labeling)
    n_seeds = len(skel_paths)

    # set all outside nodes to max seed id
    node_seeds[node_labeling != object_id] = n_seeds + 1
