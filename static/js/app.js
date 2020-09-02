
// Adding event listener for fetching result
document.querySelector('#submit').addEventListener('click', fetchResult);


async function fetchResult(e) {
    e.preventDefault();

        var rizwan = document.getElementById('mydatas');
        let fd = new FormData(rizwan);

        $.ajax({
            type: "POST",
            url: 'http://127.0.0.1:5000/data',
            data: fd, // Data sent to server, a set of key/value pairs (i.e. form fields and values)
            contentType: false, // The content type used when sending data to the server.
            cache: false, // To unable request pages to be cached
            processData: false,
            success: function (result) {
                
                let {pred1, pred2} = result;
                // let {n_bottles, n_packs, n_boxes, n_choclates, n_cpacks, n_cboxes, n_biscuits, n_bpacks, n_bboxes, } = result;
                // console.log(pred1);
                // console.log(n_packs);
                // console.log(n_boxes);
                // console.log(n_choclates);
                
                $('#bott').append(JSON.stringify(pred1));
                $('#packs').append(JSON.stringify(pred2));
                // $('#packs').append(JSON.stringify(n_packs));
                // $('#box').append(JSON.stringify(n_boxes));
                // $('#choclates').append(JSON.stringify(n_choclates));
                // $('#cpacks').append(JSON.stringify(n_cpacks));
                // $('#cbox').append(JSON.stringify(n_cboxes));
                // $('#biscuits').append(JSON.stringify(n_biscuits));
                // $('#bt_packs').append(JSON.stringify(n_bpacks));
                // $('#bt_box').append(JSON.stringify(n_bboxes));
    
             }
                
        });
    
}